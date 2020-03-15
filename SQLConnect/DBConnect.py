# 数据库连接
import pymssql
import pymysql
import psycopg2


# 定义数据库连接类
class DBConnect:

    def __init__(self, database_type):
        # 连接数据库
        try:
            if database_type == "SQL Server":
                print("准备连接SQL Server数据库……")
                # 连接数据库
                self._connect = pymssql.connect(
                    host='134.175.72.35',
                    user='sa',
                    password='123abc',
                    database='spatial_database')
                print("SQL Server数据库连接成功")
            elif database_type == "MySQL":
                print("准备连接MySQL数据库……")
                # 连接数据库
                self._connect = pymysql.connect(
                    database='spatial_database',
                    user='root',
                    password='123456',
                    host='134.175.72.35',
                    port=3306)
                print("MySQL数据库连接成功")
            elif database_type == "PostgreSQL":
                print("准备连接postgres数据库……")
                # 连接数据库
                self._connect = psycopg2.connect(
                    database='spatial_database',
                    user='postgres',
                    password='123',
                    host='134.175.72.35',
                    port='5432')
                print("postgres数据库连接成功")
        except Exception as e:
            # 输出错误原因
            print("连接失败:", e)

        # 创建游标对象
        self._cursor = self._connect.cursor()

    # 增
    def save(self, tableName, fields):
        print(fields)
        # 定义SQL语句
        sql = 'insert into ' + tableName + '('
        # 定义储存的字段数组
        field = []
        # 定义储存的值数组
        value = []
        # 定义储存的占位符数组
        placeholder = []
        # 添加字段
        for key, val in fields.items():
            # 添加要储存的字段
            field.append(key)
            # 添加要储存的值
            value.append(val)
            # 添加占位符
            placeholder.append("%s")
        # 将字段和占位符添加到SQL语句中
        sql += ",".join(field) + ")values(" + ",".join(placeholder) + ")"
        try:
            # 运行SQL语句
            self._cursor.execute(sql, tuple(value))
            # 提交到数据库执行
            self._connect.commit()
            print("储存数据成功！")
        except Exception as e:
            # 发生错误回滚
            self._connect.rollback()
            # 打印错误原因
            print("储存数据失败！失败原因：", e)

    # 删
    def remove(self, tableName, fields):
        # 定义SQL语句
        sql = 'delete from ' + tableName + " where "
        # 定义删除的字段和值
        field = []
        value = []
        for key, val in fields.items():
            field.append(key + " = %s")
            value.append(val)
        sql += " and ".join(field)
        try:
            # 运行SQL语句
            self._cursor.execute(sql, tuple(value))
            # 提交到数据库执行
            self._connect.commit()
            print("删除数据成功！")
        except Exception as e:
            # 发生错误回滚
            self._connect.rollback()
            # 打印错误原因
            print("删除数据失败！失败原因：", e)

    # 改
    def update(self, tableName, mainFields, fields):
        # 定义SQL语句
        sql = "update " + tableName + " set "
        # 定义要修改字段
        field = []
        # 定义要修改字段对应的值和限定字段
        value = []
        for key, val in fields.items():
            # 添加要修改的字段
            field.append(key + " = %s")
            # 添加要修改的值
            value.append(val)
        # 将修改字段添加到SQL语句
        sql += ", ".join(field) + " where "
        # 数组清空用来存储修改限定字段
        field = []
        for key, val in mainFields.items():
            # 添加限定字段
            field.append(key + " = %s")
            # 添加限定字段的值
            value.append(val)
        # 将限定字段添加到SQL语句
        sql += " and ".join(field)
        try:
            # 运行SQL语句
            self._cursor.execute(sql, tuple(value))
            # 提交到数据库执行
            self._connect.commit()
            print("修改数据成功！")
        except Exception as e:
            # 发生错误回滚
            self._connect.rollback()
            # 打印错误原因
            print("修改数据失败！失败原因：", e)

    # 查
    def select(self, tableName, fields, returnFields):
        # 定义查询返回字段
        if len(returnFields) == 0:
            return_str = "*"
        else:
            return_str = ",".join(returnFields)
        # 查询限定字段不存在时
        if len(fields) == 0:
            # 定义SQL语句
            sql = "select " + return_str + " from " + tableName
            try:
                # 运行SQL语句
                self._cursor.execute(sql)
                print("查找数据成功！")
                return self._cursor.fetchall()
            except Exception as e:
                # 打印错误原因
                print("查找数据失败！失败原因：", e)
                return None
            # 查询限定字段存在时
        else:
            # 定义限定字段数组
            field = []
            # 定义限定字段对应的值
            value = []
            for key, val in fields.items():
                # 向数组中添加限定字段
                field.append(key + " = %s")
                # 添加限定字段对应的值
                value.append(val)
            # 定义SQL语句
            sql = "select " + return_str + " from " + tableName + " where " + " and ".join(field)
            try:
                # 运行SQL语句
                self._cursor.execute(sql, tuple(value))
                print("查找数据成功！")
                return self._cursor.fetchall()
            except Exception as e:
                # 打印错误原因
                print("查找数据失败！失败原因：", e)
                return None

    # 关闭数据库连接
    def close_connect(self):
        # 关闭数据库连接
        self._connect.close()


if __name__ == "__main__":
    # 创建数据库连接对象
    connect = DBConnect("PostgreSQL")
    # 获取数据
    results = connect.select("test", "", "")
    # 打印数据
    print(results)
