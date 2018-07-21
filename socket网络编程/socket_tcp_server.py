#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import socketserver
import subprocess
import struct

class MySocket(socketserver.BaseRequestHandler):
    def handle(self):
        # print("socket>>>",self.request)
        # print("addr>>>",self.client_address)
        while True:
            try:
                data=self.request.recv(1024)
                if not data:break
                print("接收客户端的信息",data.decode())

                #发送信息：
                s=subprocess.Popen(data.decode(),shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                if s.stderr.read():
                    cmd_res=s.stderr.read()
                else:
                    cmd_res=s.stdout.read()
                if not cmd_res:
                    print("返回信息结果...".encode('utf-8'))

                #解决粘包的问题；
                length=len(cmd_res)
                dat_len=struct.pack("i",length)

                #发送信息：
                self.request.sendall(dat_len)
                self.request.sendall(cmd_res)
            except Exception as e:
                print(e)
                break

if __name__ == '__main__':
    IP_PORT=("127.0.0.1",8888)
    t=socketserver.ThreadingTCPServer(IP_PORT,MySocket)
    t.serve_forever()
