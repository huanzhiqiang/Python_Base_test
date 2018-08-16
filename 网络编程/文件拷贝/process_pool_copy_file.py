#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import multiprocessing
import os,shutil

def copy_file(srt_dir,dst_dir,filename):
    srt_path=srt_dir+filename
    dst_path=dst_dir+filename
    with open(srt_path,'rb') as read_file:
        with open(dst_path,'wb') as write_file:
            while True:
                    data=read_file.read(1024)
                    if data:
                        write_file.write(data)
                    else:
                        break

if __name__ == '__main__':
    srt_dir="./test/"
    dst_dir="/home/python/Desktop/test/"
    list_data=os.listdir(os.getcwd()+"/test/")
    if os.path.isdir(srt_dir):
        if not os.path.isdir(dst_dir):
            os.mkdir(dst_dir)
            pool=multiprocessing.Pool(3)
            for filename in list_data:
                #同步拷贝
                # pool.apply(copy_file,(srt_dir,dst_dir,filename))

                #异步拷贝
                pool.apply_async(copy_file,args=(srt_dir,dst_dir,filename))
            pool.close()
            pool.join()
            print("文件拷贝完成！")
        else:
            print("目标目录 已存在，清除目标目录")
            shutil.rmtree(dst_dir)
            exit()
    else:
        print("源文件不存在")
        exit()