#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import socketserver
class MyUDPServer(socketserver.BaseRequestHandler):
    def handle(self):
        print(">>socket>>",self.request)
        print("addr>>>：",self.client_address)
        try:
            #接收信息：
            data=self.request[0]
            if not data:exit()
            print("接收来自客户端的信息",data.decode())

            #发送信息：
            self.request[1].sendto(data.upper(),self.client_address)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    IP_PORT=("127.0.0.1",9999)
    s=socketserver.ThreadingUDPServer(IP_PORT,MyUDPServer)
    s.serve_forever()