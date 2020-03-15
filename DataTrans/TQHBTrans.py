from SQLConnect.DBConnect import DBConnect


# 创建天气后报网站的存取类
class TQHBTrans:

    def __init__(self):
        # 创建MySQL数据库连接对象
        self._connect = DBConnect("MySQL")

    # 保存数据函数
    def save_temp(self, temp):
        # 将数据保存到province_temp表中
        for i in range(len(temp)):
            self._connect.save("province_temp", {"province_name": temp[i][0],
                                           "date_str": temp[i][1],
                                           "low_temp": temp[i][2],
                                           "high_temp": temp[i][3]})
        # 关闭数据库连接
        self._connect.close_connect()

    # 获取数据函数
    def get_temp(self, time, filed):
        # 查询数据
        result = self._connect.select("province_temp", {"date_str": time}, ["province_name", filed])
        # 关闭数据库连接
        self._connect.close_connect()
        # 返回结果
        return result

    # 获取日期函数
    def get_date(self):
        # 获取province_temp表中所有的日期
        dates = self._connect.select("province_temp", "", ["date_str"])
        # 关闭数据库连接
        self._connect.close_connect()
        # 定义一个空数组(列表)
        time = []
        # 当数组中不存才当前日期时,向数组中添加当前日期,存在时跳过
        for dt in dates:
            if dt[0] not in time:
                time.append(dt[0])
        # 将日期从小到大排列后返回
        return sorted(time)


if __name__ == '__main__':
    # 定义天气后报网站数据存取对象
    data_trans = TQHBTrans()
    # 获取所有日期
    results = data_trans.get_date()
    # 打印结果
    print(results)
