#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from socket import *
import struct

def send_recv_client(udp_client,IP_PORT,Buffer_size):
    while True:
        try:
            cmd=input("请输入指令：").strip()
            if not  cmd:continue
            if cmd=="quit":break
            udp_client.sendto(cmd.encode(),IP_PORT)

            content,addr=udp_client.recvfrom(Buffer_size)
            print("收到数据信息",content.decode('gbk'))
        except Exception as e:
            print(e)
            break

if __name__ == '__main__':
    IP_PORT=("127.0.0.1",6666)
    Buffer_size=1024
    udp_client=socket(AF_INET,SOCK_DGRAM)
    send_recv_client(udp_client,IP_PORT,Buffer_size)


