#coding=utf-8
#import MySQLdb
import pymysql

conn= pymysql.connect(
        host='192.168.11.20',
        port = 3307,
        user='root',
        passwd='ydkj',
        db ='lngmall_test',
	charset='utf8'
        )
cur = conn.cursor()


#创建数据表
#cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

#插入一条数据
#cur.execute("insert into student values('2','Tom','3 year 2 class','9')")


#修改查询条件的数据
#cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
#cur.execute("delete from student where age='9'")

aa=cur.execute("select * from s_user limit 5")

#打印表中的多少数据
info = cur.fetchmany(aa)
for ii in info:
    print (ii)

conn.commit()
cur.close()
conn.close()
