#!/usr/bin/env python
# _*_ coding:utf-8 _*_
dist_1={"age":89,"age1":34,"age2":56,"age3":87,"age4":100,}
res=list(max(zip(dist_1.values(),dist_1.keys())))
print(res) #[100, 'age4']  #比较从第一个元素进行比较；比较出大小不会再进行下个元素的比较；
