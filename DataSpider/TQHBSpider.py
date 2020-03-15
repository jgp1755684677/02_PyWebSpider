import urllib.request as req
from bs4 import BeautifulSoup
import re


# 定义爬取天气后报网站的爬虫类
class TQHBSpider:
    _province_url = []

    # 初始化类，获取2019年省会城市历史天气的url
    def __init__(self, url):
        # 打开url链接
        web = req.urlopen(url)
        # 读取网页的数据
        html = web.read()
        # 将byte类型数据转换成字符串
        html = html.decode('gbk')
        # 将html代码转至对象
        bs = BeautifulSoup(html, 'html.parser')
        # 定义省份名字和其省会城市拼音名称的数组
        province = []
        # 定义获取省会城市拼音名称的标签
        label = r'<dd><a href="/lishi/(.*?).html"'
        for i in range(len(bs.select('dt a'))):
            # 获取省名和其对应省会拼音名称
            temp = [bs.select('dt a')[i].get_text(),
                    re.findall(label, str(bs.select('dd')[i]), re.S)[0]]
            # 将获取的数据添加至数组
            province.append(temp)
        # 定义数组用于保存省名和其对应2019年12个月历史天气的url
        for i in range(12):
            for j in range(len(province)):
                if i < 9:
                    temp_url = url + province[j][1] + '/month/20190' + str(i + 1) + '.html'
                else:
                    temp_url = url + province[j][1] + '/month/2019' + str(i + 1) + '.html'
                temp = [province[j][0], temp_url]
                self._province_url.append(temp)

    def get_data(self):
        # 定义气温数据保存数组
        temp_data =[]
        for i in range(len(self._province_url)):
            # 打开url链接
            web = req.urlopen(self._province_url[i][1])
            # 打印要获取网页的地址
            print(self._province_url[i][1])
            # 读取网页的数据
            html = web.read()
            # 将byte类型数据转换成字符串
            html = html.decode('gbk')
            # 定义获取温度区域的标签
            region_label = r'<b>风力风向</b></td>(.*?)</table>'
            # 获取返回数组的唯一值（第一个值）
            table = re.findall(region_label, html, re.S)[0]
            # 去除字符串中回车符
            table = table.replace("\r", "")
            # 去除字符串中的换行符
            table = table.replace("\n", "")
            # 去除字符串中的空格
            table = table.replace(" ", "")
            # 定义获取日期的标签
            date_label = r'>2019年(.*?)日'
            # 定义获取温度区域的标签
            temp = r'</td><td>(.*?)℃</td><td>'
            # 定义最低温度的标签
            high_temp_label = r'</td><td>(.*?)℃'
            # 定义最高温度的标签
            low_temp_label = r'℃/(.*?)℃</td>'
            # 获取时间信息
            date = re.findall(date_label, table, re.S)
            # 将日期改成年月日形式（如20190101）
            for j in range(len(date)):
                date[j] = '2019' + date[j].replace("月", '')
            # 定义最低温保存数组
            high_temp = []
            # 定义所在省份名称
            province_name = []
            for j in range(len(re.findall(temp, table, re.S))):
                # 获取最低温度
                high_temp.append(re.findall(high_temp_label, re.findall(temp, table, re.S)[j], re.S)[0])
                # 添加对应省份的名称
                province_name.append(self._province_url[i][0])
            # 获取各省最低气温
            low_temp = re.findall(low_temp_label, table, re.S)
            # 将获取的值写入数组
            for j in range(len(date)):
                # 定义一个含有上面获取四个信息的数组
                temp = [province_name[j], date[j], low_temp[j], high_temp[j]]
                # 将将获取的信息添加到一个新数组中
                temp_data.append(temp)
            # 获取数据完成
            print("该页数据获取完毕")
        # 返回获取的信息
        return temp_data


if __name__ == '__main__':
    # 爬虫网页URL
    url = 'http://www.tianqihoubao.com/lishi/'
    # 创建爬虫对象
    data = TQHBSpider(url)
    # 获取数据
    result = data.get_data()
    # 打印结果
    print(result)