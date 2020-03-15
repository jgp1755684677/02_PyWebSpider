from SQLConnect.DBConnect import DBConnect


# 定义新型肺炎数据存取类
class COVIDTrans:

    def __init__(self):
        # 创建SQL Server数据库连接对象
        self._connect = DBConnect("SQL Server")

    # 定义保存数据函数
    def save_data(self, ncov):
        # 向数据库中写入数据
        for i in range(len(ncov)):
            self._connect.save("ncov", {"province_name": ncov[i][0],
                                  "current_count": ncov[i][1],
                                  "ncov_count": ncov[i][2],
                                  "cured_count": ncov[i][3],
                                  "dead_count": ncov[i][4]})
        # 关闭数据库连接
        self._connect.close_connect()

    # 定义获取数据函数
    def get_data(self, field):
        # 查询数据
        result = self._connect.select("ncov", "", ["province_name", field])
        # 关闭数据库连接
        self._connect.close_connect()
        # 返回查询结果
        return result


if __name__ == '__main__':
    # 定义数据存取对象
    data_trans = COVIDTrans()
    # 查询现存确诊人数
    results = data_trans.get_data("current_count")
    # 打印结果
    print(results)
