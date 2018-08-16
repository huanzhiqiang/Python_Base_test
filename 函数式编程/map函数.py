#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#列表的倍数；
num=[2,4,55,1,6]
def map_test(array):
    list_1=[]
    for i in array:
        list_1.append(i**2)
    return list_1
res=map_test(num)
print(res)

#############################################
def add_one(x):
    return x+1
def reduce_one(x):
    return x-1

def map_test1(func,array):
    res=[]
    for i in array:
        res.append(func(i))
    return res
rr=map_test1(add_one,num)
rr_2=map_test1(lambda x:x**2,num)
print(rr)
print(rr_2)

##map函数实现自减一的操作；(函数式编程)
print(list(map(reduce_one,num)))  #num可以是个可迭代的对象
print(list(map(lambda x:x**2,num)))
print(list(map(add_one,num)))

#字符串转大写
msg="huanzhiqiang"
print(list(map(lambda x:x.upper(),msg)))
