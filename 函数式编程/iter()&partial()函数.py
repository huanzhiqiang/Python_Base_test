#!/usr/bin/env python
# _*_ coding:utf-8 _*_
l=['a','b','c','g','e']

def foo():
    return l.pop()
x=iter(foo,'c')
print(x.__next__())
print(x.__next__())
# print(x.__next__())  #当迭代器查找到"c"时迭代器停止；StopIteration
#iter()循环迭代只到录找固定条件时终止；

from functools import partial
def add(x,y):
    return x+y
func=partial(add,1)  #固定一个值参；
print(func)
print(func(1)) #2
print(func(2)) #3

# recv_msg=''.join(iter(partial(shell_client.recv,Buffer_size),b''))