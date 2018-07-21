#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from socket import *
import hmac

ss=b'huanzhiqiang'
def auth_client(tcp_client):
    msg=tcp_client.recv(32)
    h1=hmac.new(ss,msg)
    digest_1=h1.digest()
    tcp_client.sendall(digest_1)

def Tx_client(tcp_client,Buffer_size):
    while True:
        content=input("请输入信息:").strip()
        tcp_client.sendall(content.encode())

        data=tcp_client.recv(Buffer_size)
        print("收取服务端的信息",data.decode())

def conn_client(IP_PORT,Buffer_size):
    tcp_client=socket(AF_INET,SOCK_STREAM)
    tcp_client.connect(IP_PORT)
    auth_client(tcp_client)
    Tx_client(tcp_client,Buffer_size)

if __name__ == '__main__':
    IP_PORT=("127.0.0.1",7777)
    Buffer_size=1024
    conn_client(IP_PORT,Buffer_size)
