#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import socketserver
import subprocess

class MyUdpServer(socketserver.BaseRequestHandler):
    def handle(self):
        # print("无组数据:",self.request)
        # print("数据部分：",self.request[0])
        # print("socket部分：",self.request[1])
        # print("client:",self.client_address)
        try:
            cmd=self.request[0]
            if not cmd:exit()
            print("收到客户端的指令信息：",cmd.decode())
            s=subprocess.Popen(cmd.decode(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            if s.stderr.read():
                cmd_res=s.stderr.read()
            else:
                cmd_res=s.stdout.read()
            if not cmd_res:
                print("数据信息返回正常输出...")

            self.request[1].sendto(cmd_res,self.client_address)

        except Exception as e:
            print(e)
            exit()


if __name__ == '__main__':
    IP_PORT=("127.0.0.1",6666)
    t=socketserver.ThreadingUDPServer(IP_PORT,MyUdpServer)
    t.serve_forever()
