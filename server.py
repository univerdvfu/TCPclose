# Пример сервера

import socket

# Создаем сокет
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к адресу и порту
s.bind(('127.0.0.1', 12345))
s.listen()

    # Принимаем входящее соединение
conn, addr = s.accept()
print(conn)

try:
    


    while True:
        # Начинаем прослушивать входящие соединения
        
        # Отправляем сообщение клиенту
        conn.send(b'Hello, client!')

        # Получаем сообщение от клиента
        data = conn.recv(1024)
        print('Received from client:', data)
    # Выводим сообщение на экран
    print('Received from client:', data)

except Exception as e:
    
# Закрываем соединение
    for x in range(1000):
        print(1);
