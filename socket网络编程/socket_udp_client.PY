#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from socket import *
def UDP_Client(udp_client,IP_PORT):
    #发送信息：
    while True:
        msg=input("输入信息内容>>>>>>>").strip()
        if not msg:continue
        if msg=="quit":break
        udp_client.sendto(msg.encode(),IP_PORT)

        #接收信息：
        data,addr=udp_client.recvfrom(1024)
        print("收到来自服务端的信息",data.decode())

    udp_client.close()

if __name__ == '__main__':
    IP_PORT=("127.0.0.1",9999)
    udp_client=socket(AF_INET,SOCK_DGRAM)
    UDP_Client(udp_client,IP_PORT)
