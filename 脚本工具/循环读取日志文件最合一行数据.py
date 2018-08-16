#!/usr/bin/env python
# _*_ coding:utf-8 _*_
with open('accesslog','rb') as f:
    #1、静态文件读取方法；
    # data = f.readlines()
    # print(data[-1])

    #2、实时文件读取（大数据量下读取）
    offs = -50
    while True:
        f.seek(offs,2)
        data = f.readlines()
        print(data)
        if len(data) > 1:
            print('文件的最后一行: %s' % (data[-1]))
            break
        offs *= 2