#Python的内置HTTP请求库
#常用块：
#   urllib.request      # 请求模块
#   urllib.error        # 异常处理模块
#   urllib.parse        # URL解析模块
#   urllib.robotparser  # robots.txt解析模块

#官网文档：https://docs.python.org/3/library/urllib.html
#----------------------------------------------

# #常见示例

#获取百度页面源代码，通过get的方式
# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# import urllib.parse
# import urllib.request
# data = bytes(urllib.parse.urlencode[{'world':'hello'}],encoding='utf8')
# response = urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read())

#异常捕获,当相应超过0.1s就打印‘TIME OUT’
# import socket
# import urllib.request
# import urllib.error
#
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
# except urllib.error.URLError as e:
#     #判断错误条件
#     if isinstance(e.reason,socket.timeout):
#         print('TIME OUT')

#----------------------------------------------

# #常用的响应模块命令

# import urllib.request
# response = urllib.request.urlopen('https://www.python.org')
# #响应类型
# print(type(response))
# #状态码
# print(response.status)
# #响应头
# print(response.getheaders())
# #获取相应内容
# print(response.read().decode('utf-8'))

#----------------------------------------------

# #实现代理访问，通过配置代理IP实现页面爬取，用于切换IP
# import urllib.request
# proxy_handler = urllib.request.ProxyHandler({
#     'IP'
# })
# opener = urllib.request.build_opener(proxy_handler)
# response = opener.open('www.baidu.com')
# print(response.read())

#----------------------------------------------

#cookie相关
import http.cookiejar,urllib.request
# #声明cookie对象
# cookie = http.cookiejar.CookieJar()
# #处理cookie
# handler = urllib.request.HTTPCookieProcessor(cookie)
# #传递handler
# opener = urllib.request.build_opener(handler)
# #打开百度页面
# response = opener.open('http://www.baidu.com')
# for ltem in cookie:
#     print(ltem.name+"="+ltem.value)

# #保存cookie至文件
# filename = "cookie.txt"
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True,ignore_expires=True)

# #读取Cookie
# cookie = http.cookiejar.LWPCookieJar()
# cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))
#或使用下面方法
# cookiejar = http.cookiejar.MozillaCookieJar()
# cookiejar.load('cookie.txt')
# handler = urllib.request.HTTPCookieProcessor(cookiejar)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://wwww.baidu.com')
# print(response.read().decode('utf-8'))
#----------------------------------------------

# #异常处理
# #页面提示Not Found时调用URLError的异常处理
# from urllib import request,error
# try:
#     response = request.urlopen('http://cuiqingcai.com/index.html')
# except error.URLError as e:
#     print(e.reason)
#
# # #页面提示Not Found时调用HTTPError的异常处理
# from urllib import request,error
# try:
#     response = request.urlopen('http://cuiqingcai.com/index.html')
# except error.HTTPError as e:
#     #请求失败打印，失败原因；状态码；请求头信息
#     print(e.reason,e.code,e.headers,sep='\n')
# else:
#     print('Request Successfully')

#----------------------------------------------

# #URL解析

# #urlparse方法
# from urllib.parse import urlparse
#
# #对URL进行划分，用于对URL的拆分操作
# result = urlparse('https://blog.csdn.net/qq_24394093/article/details/82254403')
# print(type(result),result)
# #自定义协议类型，进行划分
# result2 = urlparse('blog.csdn.net/qq_24394093/article/details/82254403',scheme='https')
# print(result2)
# #向前拼接
# result3 = urlparse('https://blog.csdn.net/qq_24394093/article/details/82254403',allow_fragments=False)
# print(result3)

#----------------------------------------------

# #URL的拼接

# # 将字符串拼接为URL，但是测试时效果不佳
# from urllib.parse import urlunparse
# data = ['https','blog.csdn.net','qq_24394093','article','details','82254403']
# print(urlunparse(data))

# # 将自定的字符串，拼接到URL生成新URL
# from urllib.parse import urljoin
# print(urljoin('http://baidu.com','index.html'))
# print(urljoin('http://baidu.com','http://test.com/index.html'))

# #将字典转换为请求参数
# from urllib.parse import urlencode
# params = {
#     'name':'alien',
#     'age':'24'
# }
# base_url = 'http://www.baidu.com?'
# url = base_url + urlencode(params)
# print(url)

#----------------------------------------------

# import urllib.robotparser
# <"详细查看官网">
