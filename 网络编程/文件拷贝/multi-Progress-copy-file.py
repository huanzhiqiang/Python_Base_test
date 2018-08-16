#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os, shutil
import multiprocessing

def copy_file(srt_path, dst_path):
    with open(srt_path, 'rb') as read_f:
        with open(dst_path, 'wb') as write_f:
            while True:
                data = read_f.read(1024)
                if data:
                    write_f.write(data)
                else:
                    break


if __name__ == '__main__':
    srt_dir = '/home/python/s/'
    dst_dir = "/home/python/Desktop"
    del_dir = "/home/python/Desktop/s"
    if os.path.isdir(del_dir):
        shutil.rmtree(del_dir)
    pool = multiprocessing.Pool(3)
    for fpathe, dirs, fs in os.walk(srt_dir):
        dd = fpathe.split('python')
        dst_ll = dst_dir + dd[1]
        if not os.path.isdir(dst_ll):
            os.makedirs(dst_ll)
        else:
            print("目标文件已存在..")
            break
        for f in fs:
            srt_path = os.path.join(fpathe, f)
            dst_path = os.path.join(dst_ll, f)
            pool.apply(copy_file, args=(srt_path, dst_path))

"""
for fpathe, dirs, fs in os.walk(srt_dir):
fpathe:是源文件递归目录路径；
dirs:是递归文件目录列表；
fs: 文件的列表；

"""