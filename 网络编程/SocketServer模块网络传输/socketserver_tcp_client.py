#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import struct
from socket import *
import hmac
def send_recv_client(tcp_client,Buffer_size):
    while True:
        try:
            cmd=input("请输入指令：").strip()
            if not cmd:continue
            if cmd=="quit":break
            tcp_client.send(cmd.encode())

            date_len=tcp_client.recv(4)
            length=struct.unpack('i',date_len)[0]

            recv_size=0
            recv_content=b''
            while recv_size<length:
                recv_content +=tcp_client.recv(Buffer_size)
                recv_size=len(recv_content)

            print("收到数据信息：",recv_content.decode('gbk'))
        except Exception as e:
            print(e)
            break
    tcp_client.close()

def auth_client(tcp_client):
    ss = b'huanzhiqiang'
    msg=tcp_client.recv(32)
    h1=hmac.new(ss,msg)
    digest_1=h1.digest()
    tcp_client.sendall(digest_1)

if __name__ == '__main__':
    IP_PORT=("127.0.0.1",7777)
    Buffer_size=1024
    tcp_client=socket(AF_INET,SOCK_STREAM)
    tcp_client.connect(IP_PORT)
    auth_client(tcp_client)
    send_recv_client(tcp_client,Buffer_size)