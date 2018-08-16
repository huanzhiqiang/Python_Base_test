#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from socket import *
import os,hmac

ss=b'huanzhiqiang'
def auth_user(conn):
    dic=os.urandom(32)
    conn.send(dic)
    h1=hmac.new(ss,dic)
    digest_1=h1.digest()
    respone = conn.recv(len(digest_1))
    return hmac.compare_digest(respone,digest_1)

def TongX(conn,Buffer_size):
    if not auth_user(conn):
        print("连接不合法...")
        conn.close()
        return
    print("连接合法...")
    while True:
        try:
            data=conn.recv(Buffer_size)
            if not data:break
            print("收到客户端的信息",data.decode())
            conn.send(data.upper())
        except Exception as e:
            print(e)
            break
    conn.close()
def conn_sock(IP_PORT,Buffer_size,backlog=5):
    tcp_server=socket(AF_INET,SOCK_STREAM)
    tcp_server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    tcp_server.bind(IP_PORT)
    tcp_server.listen(backlog)
    while True:
        conn,addr=tcp_server.accept()
        print("新的客户端连接地址：",addr[0])
        TongX(conn,Buffer_size)


if __name__ == '__main__':
    IP_PORT=("127.0.0.1",7777)
    Buffer_size=1024
    conn_sock(IP_PORT,Buffer_size)