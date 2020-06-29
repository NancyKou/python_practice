import pymysql
# 链接数据库
db = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='12345678',db='employees',charset='utf-8')
#db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='mydata', charset='utf8')
# 创建游标对象cursor
cursor = db.cursor()

# 插入数据
sql = "insert into employees (emp_no,birth_date,first_name,last_name,gender,hire_date) values (%s, %s,%s, %s,%s, %s)"
for i in range(2, 101, 1):
    emp_no = "test北京地铁"+str(i)+"号线"
    cursor.execute(sql, (i, emp_no))        # 传值
    db.commit()                               # 提交事务

# 关闭数据库连接
db.close()









'''
# 查看插入后的结果
sql2 = "select * from lineinfo"
cursor.execute(sql2)
data2 = cursor.fetchone()
print("插入后lineinfo表：" + "\n", data2)

# 关闭数据库连接
db.close()

# 查询数据库版本
cursor.execute("select version()")
data = cursor.fetchone()
print(" Database Version:%s" % data)

# 删除数据
sql = "delete from lineinfo where ID>=2"
cursor.execute(sql)
db.commit()
# 查看删除后的结果
sql = "select * from lineinfo"
cursor.execute(sql)
data = cursor.fetchone()
print("删除后lineinfo表：" + "\n", data)'''