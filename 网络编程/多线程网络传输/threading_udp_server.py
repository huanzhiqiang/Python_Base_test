#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from socket import *
import struct,threading,subprocess
def send_server(udp_server,client_addr,cmd_res):
    udp_server.sendto(cmd_res,client_addr)

def recv_server(udp_server,Buffer_size):
    while True:
        try:
            cmd,client_addr=udp_server.recvfrom(Buffer_size)
            if not cmd:break
            print("接收到对方的信息",cmd.decode())

            s=subprocess.Popen(cmd.decode(),shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
            if s.stderr.read():
                cmd_res=s.stderr.read()
            else:
                cmd_res=s.stdout.read()

            if not cmd_res:
                print("数据返回正常输出...")
            send_server(udp_server,client_addr,cmd_res)
        except Exception as e:
            print(e)
            break
    udp_server.close()
if __name__ == '__main__':
    IP_PORT=("127.0.0.1",9999)
    Buffer_size=1024
    udp_server=socket(AF_INET,SOCK_DGRAM)
    udp_server.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)
    udp_server.bind(IP_PORT)
    p=threading.Thread(target=recv_server,args=(udp_server,Buffer_size))
    p.start()
