#---简介---
#Selenium是一款自动化测试工具，支持多种浏览器用于解决爬虫中需要JavaScript渲染的问题
#条件：pip install selenium

#-------------------------------------

# #基础使用，实现“登入百度页面输入python进行搜索并将搜索结果爬取至本地”
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# #生成浏览器实例
# browser = webdriver.Chrome()
# try:
#     #传入网址
#     browser.get('https://www.baidu.com')
#     #查找'kw'元素
#     input = browser.find_element_by_id('kw')
#     #发送Key至匹配的元素
#     input.send_keys('Python')
#     #发送'回车'操作
#     input.send_keys(Keys.ENTER)
#     #等待浏览器
#     wait = WebDriverWait(browser,10)
#     #等待直到'content_left'被加载出来
#     wait.until(EC.presence_of_element_located((By.ID,'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()

#-------------------------------------

# #声明浏览器对象
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser = webdriver.Edge()
# browser = webdriver.Firefox()
# browser = webdriver.Safari()
# browser = webdriver.PhantomJS()

#-------------------------------------

# #访问页面，模拟访问淘宝页面
# from selenium import webdriver
# browser = webdriver.Chrome()
# #传入访问URL
# browser.get('https://www.taobao.com')
# #打印页面源码
# print(browser.page_source)
# #关闭浏览器
# browser.close()

#-------------------------------------

# #查找元素

#单个元素
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input1 = browser.find_element_by_id('q')
input2 = browser.find_element_by_css_selector('#q')
input3 = browser.find_element_by_xpath('//*[@id="q"]')
print(input1,'\n',input2,'\n',input3)
browser.close()
# #更多常用查找方法，如下
# browser.find_element_by_name()
# browser.find_element_by_xpath()
# browser.find_element_by_link_text()
# browser.find_element_by_partial_link_text()
# browser.find_element_by_tag_name()
# browser.find_element_by_class_name()
# browser.find_element_by_css_selector()

#万能搜索，直接全局查找'find_element'，然后在后面匹配查找类型及关键字
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element(By.ID,'q')
print(input_first)
browser.close()

