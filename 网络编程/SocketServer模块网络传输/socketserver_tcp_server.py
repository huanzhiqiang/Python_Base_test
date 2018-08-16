#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import socketserver
import subprocess,struct
import os,hmac
class MyTcpServer(socketserver.BaseRequestHandler):
    def handle(self):
        if not self.auth_user():
            print("客户端连接不合法...",self.client_address)
            return
        print("客户端连接合法...",self.client_address)
        while True:
            try:
                cmd=self.request.recv(1024)
                if not cmd:break
                print("收到客户端的命令：",cmd.decode())

                s=subprocess.Popen(cmd.decode(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
                if s.stderr.read():
                    cmd_res=s.stderr.read()
                else:
                    cmd_res=s.stdout.read()
                if not cmd_res:
                    print("数据返回正常输出...")

                date_len=len(cmd_res)
                length=struct.pack('i',date_len)

                self.request.sendall(length)
                self.request.sendall(cmd_res)
            except Exception as e:
                print(e)
                break

    def auth_user(self):
        ss = b'huanzhiqiang'
        dic=os.urandom(32)
        self.request.sendall(dic)
        h1=hmac.new(ss,dic)
        digest_1=h1.digest()
        respone = self.request.recv(len(digest_1))
        return hmac.compare_digest(respone,digest_1)

if __name__ == '__main__':
    IP_PORT=('127.0.0.1',7777)
    t=socketserver.ThreadingTCPServer(IP_PORT,MyTcpServer)
    t.serve_forever()