# # 实例引入
# import requests
# response = requests.get('https://www.baidu.com')
#打印请求类型
# print(type(response))
#打印请求状态码
# print(response.status_code)
#打印响应内容
# print(response.text)
#打印Cookie
# print(response.cookies)

# 官方文档：https://3.python-requests.org/
#--------------------------------------------

# # Request各种请求
# import requests
# requests.post('http://httpbin.org/post')
# requests.put('http://httpbin.org/put')
# requests.delete('http://httpbin.org/delete')
# requests.head('http://httpbin.org/get')
# requests.options('http://httpbin.org/get')

#--------------------------------------------

# #GET请求
# import requests
#
# #基础GET请求
# response = requests.get('http://httpbin.org/get')
# print(response.text)
#
# #带参数GET请求，两种写法
# #写法一，通过'?'分割，'&'连接(不推荐)
# response = requests.get('http://httpbin.org/get?name=alien&age=24')
# print(response.text)
# #写法二，通过内置方法传入字典
# data = {
#     'name':'alien',
#     'age':'24'
# }
# response = requests.get('http://httpbin.org/get',params=data)
# print(response.text)

#--------------------------------------------

# #解析JSON
# import requests
# import json
# response = requests.get('http://httpbin.org/get')
# #首先使用JSON转
# print(type(response.text))
# print(json.loads(response.text))
# #然后再使用requests的内置方法转，发现其实两者完全一样
# print(type(response.json()))
# print(response.json())

#--------------------------------------------

# #requests保存图片视频等文件
# #获取方法
# import requests
# response = requests.get('https://github.com/favicon.ico')
# print(type(response.text),type(response.content))
# print(response.text)
# print(response.content)
#
# #保存图片至本地
# import requests
# response = requests.get('https://github.com/favicon.ico')
# with open('1.png','wb') as f:
#     f.write(response.content)
#     f.close()

#--------------------------------------------

# # 添加Headers
# #首先测试不添加请求头，请求知乎页面，此时会报400/500错误
# import requests
# response = requests.get('https://www.zhihu.com/explore')
# print(response.text)
#
# #然后添加请求头，再次访问
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
# }
# response = requests.get('https://www.zhihu.com/explore',headers=headers)
# print(response.text)

#--------------------------------------------

# #基本POST请求
# import requests
# data = {
#     'name':'alien',
#     'age':24
# }
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
# }
# response = requests.post('http://httpbin.org/post',data=data,headers=headers)
# print(response.json())

# #响应
# import requests
# response = requests.get('http://www.jd.com')
# #状态码
# print(type(response.status_code),response.status_code)
# #请求头
# print(type(response.headers),response.headers)
# #cookie
# print(type(response.cookies),response.cookies)
# #URL
# print(type(response.url),response.url)
# #历史记录
# print(type(response.history),response.history)

# #判断请求状态码
# import requests
# response = requests.get('http://www.jd.com')
#两种写法同价
# exit() if not response.status_code == 200 else print('Request Successfully')
#或
# exit() if not response.status_code == requests.codes.ok else print('Request Successfully')

#--------------------------------------------

# #文件上传
# import requests
# files = {'file':open('1.png','rb')}
# response = requests.post('http://httpbin.org/post',files=files)
# print(response.text)

#--------------------------------------------

# #获取cookie
# import requests
# response = requests.get('https://www.baidu.com')
# print(response.cookies)
# for key,value in response.cookies.items():
#     print(key+'='+value)

# # 会话维持
# import requests
# #声明session，用于维持会话
# s = requests.Session()
# #设置cookie
# s.get('http://httpbin.org/cookies/set/number/1234567890')
# #获取cookie
# response = s.get('http://httpbin.org/cookies')
# print(response.text)

# # 证书验证
# #正常情况下，验证证书失败后程序终止（当年12306官网还是个连认证证书都没有的站，如今升级了没法做实验了）
# import requests
# response = requests.get('https://www.12306.cn')
# print(response.status_code)
# #但是不重要，我们就当它此时会报SSLError错误。那么下面开始解决，添加verify参数跳过验证
# response2 = requests.get('https://www.12306.cn',verify=False)
# print(response2.status_code)
# #此时还会有警告信息，因为我们没有做验证所以，下面我们将警告信息也去掉
# import urllib3
# urllib3.disable_warnings()
# response3 = requests.get('https://www.12306.cn',verify=False)
# print(response3.status_code)
#
# #手动指定证书
# import requests
# response = requests.get('https://www.12306.cn',cert=('/xxx/server.crt','/path/key'))
# print(response.status_code)

#--------------------------------------------

# # 代理设置

# #HTTP代理
# import requests
# proxies = {
#     "http":"http://127.0.0.1:8090",
#     "https":"https://127.0.0.1:9090"
# }
# response = requests.get('http://www.taobao.com',proxies=proxies)
# print(response.status_code)
#
# #scoket代理,需要pip install 'requests[socks]'
# import requests
# proxies2 = {
#     "http":"socks5://127.0.0.1:8090",
#     "https":"socks5://127.0.0.1:9090"
# }
# response2 = requests.get('https://www.taobao.com',proxies=proxies2)
# print(response2.status_code)

#--------------------------------------------

# #超时设置
# import requests
# from requests.exceptions import ReadTimeout
# try:
#     response3 = requests.get('http://httpbin.org/get',timeout = 0.3)
#     print(response3.status_code)
# except ReadTimeout:
#     print('Timeout')

#--------------------------------------------

# #认证设置，如页面访问就需要用户密码时
# import requests
# from requests.auth import HTTPBasicAuth
# r = requests.get('http://xxx',auth=HTTPBasicAuth('username','password'))
# # 也可以通过字典导入，两种方法等价
# r = requests.get('http://xxx',auth={'username','password'})
# print(r.status_code)

#--------------------------------------------

# #异常处理
# #官方文档：https://3.python-requests.org/api/#exceptions
# #示例，注意爬虫经常需要异常处理来确保程序的稳定运行
# import requests
# from requests.exceptions import Timeout,ConnectionError,ReadTimeout
# try:
#     response = requests.get('http://www.tttt.com', timeout=0.3)
#     print(response.status_code)
# except TimeoutError:
#     print('Timeout')
# except ConnectionError:
#     print('Connection Error')
# except ReadTimeout:
#     print('The server did not send any data in the allotted amount of time.')
