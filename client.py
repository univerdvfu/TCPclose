 

import socket

# Создаем сокет
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Устанавливаем соединение с сервером
s.connect(('127.0.0.1', 12345))
while True:
# Получаем сообщение от сервера
	data = s.recv(1024)

# Выводим сообщение на экран
	print('Received from server:', data)

# Отправляем сообщение серверу
	s.send(b'Hello, server!')

# Закрываем соединение
s.close()
