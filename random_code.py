#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import random
def v_code():
    ret=""
    for i in range(18):
        num=random.randint(0,9)
        alf=chr(random.randint(32,122))
        res=str(random.choice([num,alf]))
        ret+=res
    return ret

res=v_code()
print(res)