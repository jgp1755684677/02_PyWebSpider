import urllib.request as req
import re


# 定义疫情信息爬虫类
class COVIDSpider:

    def __init__(self, url):
        # 打开url链接
        web = req.urlopen(url)
        # 读取网页的数据
        html = web.read()
        # 将byte类型数据转换成字符串
        html = html.decode('utf-8')
        # 将字符串数据存储到私有变量html中
        self._html = html

    def get_data(self):
        ncov = []
        # 定义数据目标区域的标签
        label = r'<script id="getAreaStat">(.*?)</script>'
        # 获取数据区域
        data = re.findall(label, self._html, re.S)
        # 定义省份数据区域的标签
        province_label = r'"provinceName":(.*?)"comment"'
        # 获取省份数据区域
        province_data = re.findall(province_label, data[0], re.S)
        # 定义获取省名的标签
        province_name_label = r'"provinceShortName":"(.*?)","currentConfirmedCount"'
        # 定义获取现存确诊人数的标签
        current_count_label = r'"currentConfirmedCount":(.*?),"confirmedCount"'
        # 定义获取总共确诊人数的标签
        count_label = r'"confirmedCount":(.*?),"suspectedCount"'
        # 定义获取治愈人数的标签
        cured_count_label = r'"curedCount":(.*?),"deadCount"'
        # 定义获取死亡人数的标签
        dead_count_label = r'deadCount":(.*?),'
        for i in range(len(province_data)):
            # 定义包含疫情信息的数组
            province_array = [re.findall(province_name_label, province_data[i], re.S)[0],
                              re.findall(current_count_label, province_data[i], re.S)[0],
                              re.findall(count_label, province_data[i], re.S)[0],
                              re.findall(cured_count_label, province_data[i], re.S)[0],
                              re.findall(dead_count_label, province_data[i], re.S)[0]]
            # 将疫情信息添加到数组中
            ncov.append(province_array)
        # 返回信息
        return ncov


if __name__ == '__main__':
    # 爬取网站的URl
    url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia?link=&share=&source='
    # 创建爬虫对象
    data = COVIDSpider(url)
    # 获取数据
    results = data.get_data()
    # 打印数据
    print(results)
