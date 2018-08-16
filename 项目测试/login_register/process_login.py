#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import socket,re
import db
import config
import view_html


class My_Httpsocker():
    def __init__(self,db=None):
        tcp_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcp_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
        tcp_server.bind(config.IP_PORT)
        tcp_server.listen(config.Listen_size)
        self.tcp_server=tcp_server
    @property
    def start(self):
        while True:
            new_client,addr=self.tcp_server.accept()
            print('新的客户端连接进来',addr)
            self.handle_request(new_client)

    def handle_request(self,new_client):
        recv_data =new_client.recv(config.Buffer_size)
        if not recv_data:
            print('客户端已关闭')
            new_client.close()
            return
        res_data=re.match('GET\s(.*)\sHTTP/1.1',recv_data.decode('utf8'))
        if not res_data:
            print("浏览器请求的报文格式错误!")
            new_client.close()
            return
        res_info=res_data.group(1)
        print("kkk>>>",res_info)
        if res_info=="/":
            res_info="/login.html"
        view_path={
            'PATH_VIEW':res_info
        }
        status,heards,res_content=view_html.app(view_path)

        res_line="HTTP/1.1 %s\r\n"%status

        res_head=''
        for res in heards:
            res_h='%s:%s\r\n'%res
            res_head+=res_h
        respone_data=(res_line+res_head+'\r\n').encode()+res_content
        new_client.send(respone_data)
        new_client.close()

if __name__ == '__main__':
    server=My_Httpsocker()
    server.start
