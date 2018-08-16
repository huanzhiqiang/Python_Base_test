#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from socket import *
import struct
def Client_socket(client_socket):
    while True:
        #发送指令：
        cmd=input("请输入指令>>>>:").strip()
        if not cmd:continue
        if cmd=="quit":break
        client_socket.send(cmd.encode())

        #接收数据信息：
        #解决粘包的问题：
        #1、获取数据的长度信息；
        len_data=client_socket.recv(1024)
        length=struct.unpack("i",len_data)[0]

        #2、定义值信息循环获取数据；
        recv_size=0
        recv_content=b''
        while recv_size<length:
            recv_content +=client_socket.recv(1024)
            recv_size =len(recv_content)
            print("收到服务端的信息",recv_content.decode('utf-8'))
    client_socket.close()

if __name__ == '__main__':
    IP_PORT=('192.168.129.36',8888)
    client_socket=socket(AF_INET,SOCK_STREAM)
    client_socket.connect(IP_PORT)
    Client_socket(client_socket)

