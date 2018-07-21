#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import hmac,os

#产生随机字节数：
str_1=b"huanzhiqiang"
print(os.urandom(34))
#拼接加密
t1=hmac.new(str_1,os.urandom(32))
print(t1)
#得到数字形式
print(t1.digest())

##比较二进制字节数是不是一样的；
if hmac.compare_digest(b'1',b'1'):
    print("ok")
else:
    print("w")

#收到客户端的信息
# respone=conn.recv(len(t1.digest()))
# #两个二进制字节进行比对
# return hmac.compare_digest(respone,t1.digest())
