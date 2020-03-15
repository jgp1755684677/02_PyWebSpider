from SQLConnect.DBConnect import DBConnect


class WeatherTrans:

    def __init__(self):
        # 定义PostgreSQL数据库连接对象
        self._connect = DBConnect("PostgreSQL")

    # 保存最高气温数据函数
    def save_high_temp(self, high_temp):
        # 将最高气温数据保存到high_temp表中
        for i in range(len(high_temp)):
            self._connect.save("high_temp", {"sort": high_temp[i][0],
                                       "city": high_temp[i][1],
                                       "province": high_temp[i][2],
                                       "high_temp": high_temp[i][3]})
        # 关闭数据库连接
        self._connect.close_connect()

    # 保存昼夜温差数据函数
    def save_differ_temp(self, differ_temp):
        # 将昼夜温差数据保存到differ_temp表中
        for i in range(len(differ_temp)):
            self._connect.save("differ_temp", {"sort": differ_temp[i][0],
                                         "city": differ_temp[i][1],
                                         "province": differ_temp[i][2],
                                         "differ_temp": differ_temp[i][3]})
        # 关闭数据库连接
        self._connect.close_connect()

    # 创建降水量数据保存函数
    def save_precipitation(self, precipitation):
        # 将降水量数据写入precipitation表中
        for i in range(len(precipitation)):
            self._connect.save("precipitation", {"sort": precipitation[i][0],
                                           "city": precipitation[i][1],
                                           "province": precipitation[i][2],
                                           "precipitation": precipitation[i][3]})
        # 关闭数据库连接
        self._connect.close_connect()

    # 获取数据函数
    def get_data(self, table, field):
        # 查询数据
        results = self._connect.select(table, "", ["city", "province", field])
        # 关闭数据库连接
        self._connect.close_connect()
        # 定义空数组用于存储城市和省份名称,格式为City(Province)
        name = []
        # 定义空数组用于存储值
        value = []
        # 将结果添加到上面的两个数组中
        for i in range(len(results)):
            name.append(results[i][0] + "(" + results[i][1] + ")")
            value.append(results[i][2])
        # 返回两个数组
        return name, value


if __name__ == '__main__':
    # 创建Weather存取对象
    data_trans = WeatherTrans()
    # 从precipitation表中获取降水量数据
    name, value = data_trans.get_data("precipitation", "precipitation")
    # 打印结果
    print(name, value)
