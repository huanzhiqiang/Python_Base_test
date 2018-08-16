#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import socket
##下载文件代码；
from socket import *
import os

IP_PORT = ("127.0.0.1", 8889)
Buffer_size = 1024
Back_log = 5

file_server = socket(AF_INET, SOCK_STREAM)
file_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
file_server.bind(IP_PORT)
file_server.listen(Back_log)

while True:
    print("服务器已连接...")
    conn, addr = file_server.accept()
    print(addr)
    try:
        while True:
            print("文件准备...")
            file_name = conn.recv(Buffer_size)
            if not file_name: break
            if os.path.isfile(file_name.decode()):
                with open(file_name.decode(), 'rb') as r_file:
                    while True:
                        r_data = r_file.read(Buffer_size)
                        if r_data:
                            conn.send(r_data)
                        else:
                            print("读取完成！")
                            break
            else:
                conn.send("rr".encode('utf-8'))
    except Exception as e:
        print(e)
        break
    conn.close()
file_server.close()
