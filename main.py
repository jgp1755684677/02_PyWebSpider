from DataSpider.COVIDSpider import COVIDSpider
from DataSpider.TQHBSpider import TQHBSpider
from DataSpider.WeatherSpider import WeatherSpider

from DataTrans.COVIDTrans import COVIDTrans
from DataTrans.TQHBTrans import TQHBTrans
from DataTrans.WeatherTrans import WeatherTrans

from DataShow.COVIDShow import cov_show
from DataShow.TQHBShow import temp_show
from DataShow.WeatherShow import weather_show

if __name__ == '__main__':
    print("-------------开始爬取数据--------------")
    # 定义新型肺炎网站的url
    cov_url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia?link=&share=&source='
    # 定义爬虫对象
    cov_html = COVIDSpider(cov_url)
    # 获取新型肺炎数据
    cov_data = cov_html.get_data()
    # 将数据保存到数据库
    COVIDTrans().save_data(cov_data)
    print("-------------肺炎数据爬取并保存完毕--------------")

    # 定义天气后报网站url
    tq_url = 'http://www.tianqihoubao.com/lishi/'
    # 定义爬虫对象
    tq_html = TQHBSpider(tq_url)
    # 获取2019各省会天气数据
    tq_data = tq_html.get_data()
    # 将数据保存到数据库中
    TQHBTrans().save_temp(tq_data)
    print("-------------2019年各省会天气数据爬取并保存完毕--------------")

    # 定义天气网url
    weather_url = 'http://www.weather.com.cn/'
    # 定义爬虫对象
    weather_html = WeatherSpider(weather_url)
    # 获取最高温数据
    high_temp = weather_html.get_high_temp()
    # 将数据保存到数据库中
    WeatherTrans().save_high_temp(high_temp)
    # 获取昼夜温差数据
    differ_temp = weather_html.get_differ_temp()
    # 将数据保存到数据库中
    WeatherTrans().save_differ_temp(differ_temp)
    # 获取降水量数据
    precipitation = weather_html.get_precipitation()
    # 将降水量数据保存到数据库中
    WeatherTrans().save_precipitation(precipitation)
    print("-------------最高气温、昼夜温差、降水量TOP10数据爬取并保存完毕--------------")

    print("-------------开始绘图--------------")
    cov_show("Results/COVID.html")
    print("-------------肺炎数据绘图成功--------------")
    temp_show("low_temp", "最低气温", "Results/low_temp.html")
    temp_show("high_temp", "最高气温", "Results/high_temp.html")
    print("-------------最高气温、最低气温绘图成功--------------")
    weather_show("Results/Weather.html")
    print("-------------最高气温、昼夜温差、降水量图绘制成功--------------")
