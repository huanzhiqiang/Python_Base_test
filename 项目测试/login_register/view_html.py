#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import re
import db

def index(res_path):
    with open('static'+res_path,'rb') as r_file:
        respone_content=r_file.read()
        return respone_content

def login(res_path):
    if res_path=="/login.html":
        with open('static'+res_path,'rb') as r_file:
            respone_content = r_file.read()
            return respone_content
    else:
        re_data = re.findall(r"\/login\?(.*)", res_path)
        data_list = re_data[0].split("&")
        data_dict = dict([data_list[0].split("="), data_list[1].split("=")])

        username = data_dict["username"]
        password = data_dict["password"]
        print(">>>>>>>>>>>",username,password)

        # 用户填写的数据不全的时候
        if not all([username, password]):
            print("用户请求的数据不完成")
            respone_content=index("/nothings.html")
            return respone_content

        result=db.get_info(username,password)
        if result:
            respone_content=index("/index.html")
            return respone_content

        else:
            db.insert_info((username, password))
            print("注册成功------" + username + "------" + password)
            respone_content = index("/registered.html")
            return respone_content


#url
# app_list = [
#     ('/login.html',login)
# ]

def app(view_path):
    res_path=view_path['PATH_VIEW']
    if res_path.startswith("/login"):
        return '200 ok',[('Server','PY/1.1')],login(res_path)
    elif res_path.endswith('.css') or res_path.endswith('.js'):
        return '200 ok', [('Server', 'PY/1.1')], index(res_path)
    else:
        return '404 NOT FOUND',[('Server','PY/1.1')],'I WORKS!'.encode('utf8')