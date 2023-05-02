import psutil
import socket
connections = psutil.net_connections()
active_connections = [conn for conn in connections if conn.status == psutil.CONN_ESTABLISHED]
remote_ip = "127.0.0.1"
remote_port = 12345

matching_connections = [conn for conn in active_connections if conn.raddr.ip == remote_ip and conn.raddr.port == remote_port]

if matching_connections:
    connection = matching_connections[0]
else:
    print(f"No active connection found for {remote_ip}:{remote_port}")

connection.pid # ID процесса, управляющего соединением
connection.fd # файловый дескриптор сокета
psutil.Process(connection.pid).send_signal(psutil.signal.SIGTERM) # отправляем сигнал SIGTERM процессу

#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#sock.connect((connection.raddr.ip, connection.raddr.port))
#sock.shutdown(socket.SHUT_RDWR)
#sock.close()
print(connection)