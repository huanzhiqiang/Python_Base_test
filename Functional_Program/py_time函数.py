#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import time
#时间1970年：00点；
print(time.time())

##结构化时间；
print(time.localtime())
print(time.localtime(1331730421))
t=time.localtime()
print(t.tm_year,t.tm_wday)
#按时区的打印时间；
print(time.gmtime())


#将结构化时间转换成时间戳
print(time.mktime(time.localtime()))

#将结构化时间转字符串时间；
print(time.strftime("%Y-%m-%d %X",time.localtime()))
#2018-07-16 16:57:12
#字符串时间转结构化时间；
print(time.strptime("2016:12:24:17:50:35","%Y:%m:%d:%X"))
#time.struct_time(tm_year=2016, tm_mon=12, tm_mday=24, tm_hour=17, tm_min=50, tm_sec=35, tm_wday=5, tm_yday=359, tm_isdst=-1)
#时间固定格式；
print(time.asctime())#Mon Jul 16 16:57:12 2018
print(time.ctime()) #Mon Jul 16 16:57:12 2018

####datetime
import datetime
print(datetime.datetime.now()) #2018-07-16 17:02:18.303400