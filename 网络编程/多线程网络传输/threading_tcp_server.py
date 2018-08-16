#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import threading
from socket import *
import subprocess,struct
import hmac,os

#验证客户端连接的合法性；
ss=b'huanzhiqiang'
def auth_user(new_client):
    dic=os.urandom(32)
    new_client.send(dic)
    h1=hmac.new(ss,dic)
    digest_1=h1.digest()
    respone = new_client.recv(len(digest_1))
    return hmac.compare_digest(respone,digest_1)

#发送数据信息交互：
def send_tcp(new_client,cmd_res):
    data_len=len(cmd_res)
    length=struct.pack('i',data_len)

    new_client.send(length)
    new_client.send(cmd_res)

#收取tcp的报文信息：
def recv_tcp(new_client,Buffer_size):
    if not auth_user(new_client):
        print("连接用户不合法...")
        new_client.close()
        return
    print("连接用户合法...")
    while True:
        try:
            cmd=new_client.recv(Buffer_size)
            print("收到客户端的指令：",cmd.decode())
            if not cmd:break
            s=subprocess.Popen(cmd.decode(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            err=s.stderr.read()
            if err:
                cmd_res=err
            else:
                cmd_res=s.stdout.read()
            if not cmd_res:
                print("数据返回正常...")
            send_tcp(new_client,cmd_res)
        except Exception as e:
            print(e)
            break
    new_client.close()


if __name__ == '__main__':
    IP_PORT=("127.0.0.1",8980)
    Buffer_size=1024
    listen_size=128
    tcp_server=socket(AF_INET,SOCK_STREAM)
    tcp_server.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)
    tcp_server.bind(IP_PORT)
    tcp_server.listen(listen_size)
    while True:
        new_client,addr=tcp_server.accept()
        print("服务器已建立与%s连接..."%str(addr))
        p=threading.Thread(target=recv_tcp,args=(new_client,Buffer_size))
        p.start()
    tcp_server.close()