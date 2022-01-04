# -*- coding = UTF-8 #-*-
# @Time : 2021/12/15 2:21 下午
# @Author : 李宇博
# @File : testSqlite.py
# @SoftWare : PyCharm

import sqlite3
conn = sqlite3.connect("test.db")
print("Opened database successfully")
c = conn.cursor()
# sql = "create table company(id int primary key not null," \
#       "name text not null," \
#       "age int not null," \
#       "address char(50)," \
#       "salary real);"
sql = "insert into company(id,name,age,address,salary)" \
      "values(1,'张三',32,'成都',8000)"
c.execute(sql)
conn.commit()
print("Establish scheme successfully")
conn.close()


