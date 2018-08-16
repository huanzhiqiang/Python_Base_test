#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from socket import *
import struct
import hmac

#验证连接服务端的合法性；
ss=b'huanzhiqiang'
def auth_client(tcp_client):
    msg=tcp_client.recv(32)
    h1=hmac.new(ss,msg)
    digest_1=h1.digest()
    tcp_client.sendall(digest_1)

def send_recv_client(tcp_client,Buffer_size):
    while True:
        try:
            msg=input("请输入命令指令：").strip()
            if not msg:continue
            if msg=="quit":break
            tcp_client.send(msg.encode())

            data_len=tcp_client.recv(4)
            length=struct.unpack('i',data_len)[0]

            recv_size=0
            recv_content=b''
            while recv_size<length:
                recv_content +=tcp_client.recv(Buffer_size)
                recv_size=len(recv_content)
            print("收取信息是：\n",recv_content.decode('gbk'))
        except Exception as e:
            print(e)
            break
    tcp_client.close()

if __name__ == '__main__':
    IP_PORT=("127.0.0.1",8980)
    Buffer_size=1024
    tcp_client=socket(AF_INET,SOCK_STREAM)
    tcp_client.connect(IP_PORT)
    auth_client(tcp_client)
    send_recv_client(tcp_client,Buffer_size)