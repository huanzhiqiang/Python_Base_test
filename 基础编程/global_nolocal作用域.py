#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量
"""
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
print(make_counter()())
######################################################
def scope_test():
    def do_local():
        spam = "local spam" #此函数定义了另外的一个spam字符串变量，并且生命周期只在此函数内。此处的spam和外层的spam是两个变量，如果写出spam = spam + “local spam” 会报错
    def do_nonlocal():
        nonlocal  spam        #使用外层的spam变量
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"

    do_local()
    print("After local assignmane:", spam) #test spam
    do_nonlocal()
    print("After nonlocal assignment:", spam) #nonlocal spam
    do_global()
    print("After global assignment:", spam)  #nonlocal spam


scope_test()
print("In global scope:", spam) #global spam
