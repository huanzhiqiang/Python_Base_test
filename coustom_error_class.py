#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#方法一、
class AgeError(Exception):
    def __init__(self,msg):
        self.msg=msg
        super().__init__("AgeError: "+msg)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def print_age(self,age):
        try:
            if age >=0 and age <=180:
                self.__age=age
                print("正常年龄在%s"%self.__age)
            else:
                raise AgeError("请将年龄设置在0到180之间...")
        except AgeError as e:
            print(e)

p=Person('小明',18)
p.print_age(186)

#方法二；
class AgeErrors(Exception):
    def __init__(self,msg):
        self.msg=msg

    def __str__(self):
        return self.msg

class Persons:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def print_age(self,age):
        try:
            if age >=0 and age<=180:
                self.__age=age
            else:
                raise AgeErrors("AgeError: 请将年龄设置在0~180之间...")
        except AgeErrors as e:
            print(e)

p2=Persons('小明',18)
p2.print_age(186)


