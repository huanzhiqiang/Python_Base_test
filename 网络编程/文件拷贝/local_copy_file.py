#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import multiprocessing
import os,shutil

def copy_file(str_dir,dst_dir,filename):
    str_path=str_dir+filename
    dst_path=dst_dir+filename
    with open(str_path,'rb') as read_file:
        with open(dst_path,'wb')as write_file:
            while True:
                data=read_file.read(1024)
                if data:
                    write_file.write(data)
                else:
                    break


if __name__ == '__main__':
    str_dir="./test/"
    dst_dir="/home/python/Desktop/test/"
    list_file=os.listdir(os.getcwd()+"/test/")
    if list_file:
        if not os.path.isdir(dst_dir):
            os.mkdir(dst_dir)
            for filename in list_file:
                p=multiprocessing.Process(target=copy_file,args=(str_dir,dst_dir,filename))
                p.start()
            print("文件拷贝完成")
        else:
            print("目录文件已存在！清除目录")
            shutil.rmtree(dst_dir)
            exit()
    else:
        print("源文件不存在！")
        exit()
"""
    子进程文件拷贝；
"""

