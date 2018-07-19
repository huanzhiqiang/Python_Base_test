#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from functools import reduce
num_1=[1,2,3]
# res=0
# for i in num_1:
#     res += i
# print(res)
###############函数
# def foo(array):
#     res=0
#     for i in array:
#         res += i
#     return res
# print(foo(num_1))

######多条件运算；
# def C_J(x,y):
#     return x*y
# def foo(func,array):
#     res=array.pop(0)
#     for i in array:
#         res=func(res,i)
#     return res
# print(foo(C_J,num_1))

#############lambda函数；
# def foo(func,array):
#     res=array.pop(0)
#     for i in array:
#         res=func(res,i)
#     return res
# print(foo(lambda x,y:x*y,num_1))

###reduce函数；
"""
map：处理序列中的每个元素，得到结果是一个"列表"，该"列表"元素个数及位置与原来一样；
filter: 遍历序列中的每个元素，判断每个元素得到一个布尔值，如果是True则留下来；
reduce: 合并系列，得到一个最终的结果；
"""
#reduce函数；
print(reduce(lambda x,y:x*y,num_1))

##reduce实现1~100的和；
print(reduce(lambda x,y:x+y,range(1,101)))