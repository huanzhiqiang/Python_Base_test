#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#基于tcp创建文件下载；
# import socket
from socket import *
IP_PORT=("127.0.0.1",8889)
Buffer_size=1024
file_client=socket(AF_INET,SOCK_STREAM)
file_client.connect(IP_PORT)
while True:
    print("开始下载文件...")
    try:
        msg=input("请输入文件名：").strip()
        if not msg:continue
        file_client.send(msg.encode())
        with open("msg1",'ab') as w_f:
            while True:
                data=file_client.recv(Buffer_size)
                if data.decode('utf-8') =="rr":
                    print("文件不存在")
                else:
                    if data:
                        w_f.write(data)
                        print("写文件完成 ")
                        break
    except Exception as e:
        print(e)
        break

file_client.close()
