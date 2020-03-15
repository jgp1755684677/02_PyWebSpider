# 测试Urllib3、BeautifulSoup4
import urllib.request as req
from bs4 import BeautifulSoup


# 获取html网页的全部内容
def get_content(url):
    # 根据url访问网页
    web = req.urlopen(url)
    # 读取网页的数据
    html = web.read()
    # 将byte类型数据转换成字符串
    html = html.decode('utf-8')
    # 返回html数据
    return html


# 测试BeautifulSoup4
def get_data(html):
    # 将html代码转至对象
    bs = BeautifulSoup(html, 'html.parser')
    # 获取class为rank的div标签
    print(bs.find_all('div', class_='rank'))


# 主函数
if __name__ == '__main__':
    # 爬虫目标网站
    url = 'http://www.weather.com.cn'
    html = get_content(url)
    get_data(html)
