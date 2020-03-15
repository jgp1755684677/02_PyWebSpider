# # 引入pymssql包
# import pymssql
# # 连接SQL Server数据库
# connect = pymssql.connect(
#                 host='134.175.72.35',
#                 user='sa',
#                 password='123abc',
#                 database='spatial_database')
# print("SQL Server数据库连接成功")
# # 定义游标
# cursor = connect.cursor()
# # 使用execute()方法执行SQL语句
# cursor.execute("select * from test")
# # 获取所有查询结果
# results = cursor.fetchall()
# # 打印结果
# print(results)
# # 关闭数据库连接
# connect.close()


# # 引入pymysql包
# import pymysql
# # 连接MySQL数据库
# connect = pymysql.connect(
#     database='spatial_database',
#     user='root',
#     password='123456',
#     host='134.175.72.35',
#     port=3306)
# print("MySQL数据库连接成功")
# # 定义游标
# cursor = connect.cursor()
# # 使用execute()方法执行SQL语句
# cursor.execute("select * from test")
# # 获取所有查询结果
# results = cursor.fetchall()
# # 打印结果
# print(results)
# # 关闭数据库连接
# connect.close()


# 引入psycopg2包
import psycopg2
# 连接PostgreSQL数据库
connect = psycopg2.connect(
    database='spatial_database',
    user='postgres',
    password='123',
    host='134.175.72.35',
    port='5432')
print("PostgreSQL数据库连接成功")
# 定义游标
cursor = connect.cursor()
# 使用execute()方法执行SQL语句
cursor.execute("select * from test")
# 获取所有查询结果
results = cursor.fetchall()
# 打印结果
print(results)
# 关闭数据库连接
connect.close()


