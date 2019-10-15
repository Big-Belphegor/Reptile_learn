import requests
response = requests.get('http://www.baidu.com')

#获取相应页面源码
# print(response.text)

#获取请求头
# print(response.headers)

#获取状态码
# print(response.status_code)

#抓取图片
# image = requests.get('https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/static/protocol/https/home/img/qrcode/zbios_09b6296.png')
# print(image.content)

#保存抓取的图片
# with open('1.png','wb') as f:
#     f.write(image.content)
#     f.close()

from selenium import webdriver
#注意：webdriver需要下载对应的浏览器插件
#chromedriver下载地址：http://npm.taobao.org/mirrors/chromedriver
#chromedriver对应Chrome版本：https://blog.csdn.net/BinGISer/article/details/88559532
#下载后放置对应的项目目录下，或放置Python安装目录下
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
#打印百度页面的源代码
print(driver.page_source)