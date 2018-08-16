#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
from contextlib import contextmanager
from pymysql import connect
import time

@contextmanager
def mysql():
    conn=connect(host='localhost',port=3306,db='stock_db',user='root',password='mysql',charset='utf8')
    cur=conn.cursor()
    yield cur

    conn.commit()
    #关闭资源
    cur.close()
    conn.close()


def inner(ret_path):
    with open('static'+ret_path,'rb') as r_f:
        res=r_f.read()
    return res

####template
def tm_index(ret_path):
    with open('template'+ret_path) as file:
        html_data=file.read()

    ###db
    with mysql() as cur:
        sql='select * from info;'
        cur.execute(sql)

        data_from_mysql=''
        for line in cur.fetchall():
            line_str = """<tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td><input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007"></td>
            </tr>""" % line
            data_from_mysql +=line_str
    ####replace
    html_data=html_data.replace('{%content%}',data_from_mysql).encode('utf8')

    return html_data

def center(ret_path):
    with open('template' + ret_path) as r_file:
        html_data=r_file.read()

    with mysql() as cur:
        sql = "select i.code,i.short,i.chg,i.turnover,i.price,i.highs,focus.note_info from focus inner join info i on focus.info_id = i.id;"
        cur.execute(sql)

        data_from_mysql=''
        for line in cur.fetchall():
            line_str = """<tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td><a type="button" class="btn btn-default btn-xs" href="/update/000007.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a></td>
                        <td> <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="000007"></td>
                    </tr>""" % line
            data_from_mysql += line_str
    html_data=html_data.replace('{%content%}',data_from_mysql).encode('utf8')
    return html_data

app_list=[
    ("/index.html",inner),
    ("/index2.html",inner),
    ("/grand.html",inner),
    ("/tmp_index.html",tm_index),
    ("/center.html",center)
]

def app(path_app):
    ret_path=path_app['PATH_APP']
    for path,func in app_list:
        if ret_path==path:
            return '200 OK', [('Server', 'PWS5.0')],func(ret_path)
    else:
        # 状态 响应头 响应体
        return '404 Not Found',[('Server', 'PWS5.0')],"response body from app".encode('gbk')

# if __name__ == '__main__':
#     path_app={
#         'PATH_APP':'/tmp_index.html'
#     }
#     res=app(path_app)
#     print(res)