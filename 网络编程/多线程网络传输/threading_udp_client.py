#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from socket import *
import struct,threading

def send_recv_client(udp_client,Buffer_size,IP_PORT):
    while True:
        try:
            cmd=input("请输入指令：").strip()
            if not cmd:continue
            if cmd == "quit":break
            udp_client.sendto(cmd.encode(),IP_PORT)

            content,addr=udp_client.recvfrom(Buffer_size)
            print("收到信息的回复：",content.decode('gbk'))
        except Exception as e:
            print(e)
            break

    udp_client.close()
if __name__ == '__main__':
    IP_PORT=('127.0.0.1',9999)
    Buffer_size=1024
    udp_client=socket(AF_INET,SOCK_DGRAM)
    send_recv_client(udp_client,Buffer_size,IP_PORT)

