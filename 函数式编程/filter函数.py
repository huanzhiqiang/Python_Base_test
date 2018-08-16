#!/usr/bin/env python
# _*_ coding:utf-8 _*_
movie_pople=["s_hive",'hehe','s_jack','s_devior','huan']
#####1、函数式过滤；单一功能 ；
# def filter_test(array):
#     li=[]
#     for i in array:
#         if not i.startswith('s'):
#             li.append(i)
#     return li
# print(filter_test(movie_pople))

##2、通过多个函数功能接入过滤；
# def end_s(array):
#     return array.startswith('s')
# def start_s(array):
#     return array.endswith('s')
# def filter_test(func,array):
#     li=[]
#     for i in array:
#         if not func(i):
#             li.append(i)
#     return li
# res=filter_test(end_s,movie_pople)
# print(res)

###3、通过lambda函数取代多函数的定义；
# def filter_test(func,array):
#     li=[]
#     for i in array:
#         if not func(i):
#             li.append(i)
#     return li
# res=filter_test(lambda n:n.startswith('s'),movie_pople)
# print(res)

#filter函数；
rr=filter(lambda n:not n.startswith('s'),movie_pople)
print(rr.__next__()) #单取一个结果；是个可迭代的；

res1=(list(filter(lambda n:not n.startswith('s'),movie_pople)))
print(res1)


#例：
people=(
    {"name":"hehe","age":1000},
    {"name":"hh","age":1002},
    {"name":"jj","age":1003},
    {"name":"kk","age":18}
)
print(list(filter(lambda x:x['age']<=18,people)))
#[{'name': 'kk', 'age': 18}]