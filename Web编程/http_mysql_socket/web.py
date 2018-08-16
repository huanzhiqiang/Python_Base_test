#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import socket
import threading
import multiprocessing
import re,sys
import Application

class Web_Http:
    def __init__(self,IP_PORT,Buffer_size,Listen_size):
        self.IP_PORT=IP_PORT
        self.Buffer_size=Buffer_size
        self.Listen_size=Listen_size
        tcp_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcp_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
        tcp_server.bind(self.IP_PORT)
        tcp_server.listen(self.Listen_size)
        self.tcp_server=tcp_server


    def start(self):
        while True:
            new_client,addr=self.tcp_server.accept()
            print("新客户端连接",addr)
            self.http_server(new_client)


    def http_server(self,new_client):
        web_c=new_client.recv(self.Buffer_size)
        # print(">>>>>>>>>>>>",web_c.decode())
        if not web_c:
            print("浏览器可能已经关闭!~")
            new_client.close()
            return

        res_data=re.match('GET\s(.*)\sHTTP/1.1',web_c.decode())
        if not res_data:
            print("浏览器请求的报文格式错误!")
            new_client.close()
            return

        res_path=res_data.group(1)
        print(">>>>>>>>>>>>",res_path)
        if res_path=="/":
            res_path="static/index.html"
        ##动态页
        if res_path.endswith(".html"):
            path_app={
                'PATH_APP':res_path
            }
            status,headers,response_body=Application.app(path_app)
            res_line="HTTP/1.1 %s\r\n" %status

            res_heard=""
            for heard in headers:
                res_heard +="%s:%s\r\n" % heard

            rr_data=(res_line+res_heard+"\r\n").encode('utf8')+response_body
            new_client.send(rr_data)
            new_client.close()
        else:
            #静态页
            try:
                with open('static'+res_path,'rb') as r_f:
                    res_content=r_f.read()
            except Exception as e:
                res_line='HTTP/1.1 404 ok\r\n'
                res_content='%s...'%e
            else:
                res_line='HTTP/1.1 200 ok\r\n'
            finally:
                res_heard = 'Server:python/5.0\r\n'
                res_sc='\r\n'
                rr_data=(res_line+res_heard+res_sc).encode('utf8')+res_content
                new_client.send(rr_data)
                new_client.close()

def main():
    IP_PORT=('127.0.0.1',8888)
    Buffer_size=1024
    Listen_size=128
    web=Web_Http(IP_PORT,Buffer_size,Listen_size)
    web.start()

if __name__ == '__main__':
    main()
