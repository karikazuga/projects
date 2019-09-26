import socket
import os
import fcntl
import socket
import select
import threading as th

HOST = "192.168.4.182"
PORT = 5000

client =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.connect((HOST, PORT))

user = input("Введите логин>>")
fcntl.fcntl(client, fcntl.LOCK_NB)
client.send(user.encode("utf-8"))
while True:
    message = input("Введите сообщение>>")
    data = f"User:{user}\r\n{message}\n"
    try:
        client.send(user.encode("utf-8"))
    except Exception as e:
        print()
    try:
        request = client.recv(2048)
    except Exception as e:
        print(e)
    else:
        if request:
            
    
    print(request.decode("utf-8"))
