#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
from contextlib import contextmanager
from pymysql import *
from config import *

@contextmanager
def mysql():
    conn=connect(**configure)
    cur=conn.cursor()
    yield cur

    conn.commit()
    cur.close()
    conn.close()

def get_info(user_name,password):
    with mysql() as cur:
        row_data=cur.execute("select * from user where name=%s and password=%s", (user_name, password))
        if row_data:
            return cur.fetchall()
        else:
            return

def insert_info(user_info):
    with mysql() as cur:
        cur.execute("insert into user values(0,%s,%s)", user_info)
    return '插入数据成功'