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
#
# #单个元素
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input1 = browser.find_element_by_id('q')
# input2 = browser.find_element_by_css_selector('#q')
# input3 = browser.find_element_by_xpath('//*[@id="q"]')
# print(input1,'\n',input2,'\n',input3)
# browser.close()
# #更多常用查找方法，如下
# browser.find_element_by_name()
# browser.find_element_by_xpath()
# browser.find_element_by_link_text()
# browser.find_element_by_partial_link_text()
# browser.find_element_by_tag_name()
# browser.find_element_by_class_name()
# browser.find_element_by_css_selector()
#
# #通用搜索，直接全局查找'find_element'，然后在后面匹配查找类型及关键字，就是By.ID/name/xpath等
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input_first = browser.find_element(By.ID,'q')
# print(input_first)
# browser.close()
#
# #多个元素
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# lis = browser.find_elements_by_css_selector('.service-bd li a')
# print(lis)
# browser.close()

#-------------------------------------

# # 元素交互操作

# #模拟搜索操作
# from selenium import webdriver
# import time
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# #首先定位到'id=q'的地方，其实就是搜索地址栏
# input = browser.find_element_by_id('q')
# #传入'Iphone XS'到搜索栏
# input.send_keys('Iphone XS')
# #睡1s
# time.sleep(1)
# #清除搜索栏
# input.clear()
# #再输入'Ipad'
# input.send_keys('Ipad')
# #最后定位到'class=btn-search'的地方，其实就是搜索的按钮
# button = browser.find_element_by_class_name('btn-search')
# #执行点击操作，此时页面就会开始搜索IPad
# button.click()

# #下拉页面至最下面，并弹出提示窗口
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')

#-------------------------------------

# #获取元素信息
# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# logo = browser.find_element_by_id('root')
# print(logo)
# print(logo.get_attribute('class'))

#-------------------------------------

# #获取文本值
# from selenium import webdriver
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# input = browser.find_element_by_class_name('Button ExploreHeader-askButton Button--primary Button--blue')
# #获取包裹的文字
# # print(input.text)
# #获取ID
# print(input.id)
# #获取位置
# print(input.location)
# #获取标签名称
# print(input.tag_name)
# #获取大小
# print(input.size)

#-------------------------------------

# # #Frame
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchAttributeException
#
# browser = webdriver.Chrome()
# browser.get(url='https://login.tmall.com/?spm=875.7931836/B.a2226mz.1.66144265mfzVzx&redirectURL=https%3A%2F%2Fwww.tmall.com%2F')
# #进入名为'J_loginIframe'的父类
# browser.switch_to.frame('J_loginIframe')
# #查找该类下的一个元素
# source = browser.find_element_by_class_name('login-switch')
# print(source)
# try:
# #查找其它元素，如果没有则返回上级父类
#     logo = browser.find_element_by_class_name('iconfont static')
# except NoSuchAttributeException:
#     print('No iconfont static')
# #返回上级父类
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('iconfont static')
# print(logo.text)

#-------------------------------------

# #元素等待
#
# #隐式等待，当WebDriver没有在DOM中找到元素时会继续等待，当超出设定时间后再抛出异常。
# from selenium import webdriver
# browser = webdriver.Chrome()
# #隐式等待方法，此处等待10s，默认为0s
# browser.implicitly_wait(10)
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)
#
# #显示等待，当某个条件成立才去获取元素，也可以设置最大等待时间，超出后才会抛出异常。
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# wait = WebDriverWait(browser,10)
# input = wait.until(EC.presence_of_element_located((By.ID,'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))
# print(input,button)
#
# title_is                        #标题是内容
# title_contains                  #标题包含某内容
# presence_of_element_located     #元素加载处，传入定位元组，如(By.ID,'q')
# visibility_of_element_located   #元素可见，传入定位元组
# visibility_of                   #可见，传入元素对象
# presence_of_all_elements_located        #所有元素加载处
# text_to_be_present_in_element           #某元素文本包含某文字
# text_to_be_present_in_element_value     #某元素值包含某文字
# frame_to_be_available_and_switch_to_it  #frame加载并切换
# invisibility_of_element_located     #元素不可见
# element_to_be_clickable             #元素可点击
# staleness_of                        #判断一个元素是否仍在DOM，可判断页面是否已经刷新
# element_to_be_selected              #元素可选择，传元素对象
# element_located_to_be_selected      #元素可选择，传入定位元组
# element_selection_state_to_be       #传入元素对象以及状态，相等范围True，反正返回False
# element_located_selection_state_to_be   #传入定位元组以及状态，相等范围True，反正返回False
# alert_is_present                        #是否出现Alert

#-------------------------------------

# #浏览器页面的前进及后退
# import time
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.get('https://www.taobao.com')
# browser.get('https://www.python.org')
# #后退页面
# browser.back()
# time.sleep(1)
# #前进页面
# browser.forward()
# browser.close()

#-------------------------------------

# #登入天猫帐户

# from selenium import webdriver
# from selenium.webdriver import ActionChains
# import time
# #-----实例化一个Chrome
# browser = webdriver.Chrome()
# browser.implicitly_wait(3)
# browser.get('https://tmall.com')
# #-----切换至登入页面
# button_login_info = browser.find_element_by_id('login-info')
# button_login_info.click()
# time.sleep(3)
# #-----使用用户名密码的方式登入
# browser.switch_to.frame('J_loginIframe')
# js = "document.getElementById('J_Quick2Static').click()"
# browser.execute_script(js)
# browser.find_element_by_id('TPL_username_1').send_keys('南宫轩言0')
# browser.find_element_by_id('TPL_password_1').send_keys('service123')
# #-----验证(验证部分存在问题，待解决)
# start = browser.find_element_by_id('nc_1_n1z')
# actions = ActionChains(browser)
# actions.perform()
# #-----登入
# browser.find_element_by_id('J_SubmitStatic').click()

#-------------------------------------

# #Cookies
#
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())

#-------------------------------------

# #选项卡管理
#
# import time
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# #使用JS代开一个新的选项卡
# browser.execute_script('window.open()')
# print(browser.window_handles)
# #切换至第2个选项卡
# # browser.switch_to_window(browser.window_handles[1])
# browser.switch_to.window(browser.window_handles[1])
# #浏览淘宝页面
# browser.get('https://www.taobao.com')
# time.sleep(1)
# #再切换至第1个选项卡
# # browser.switch_to_window(browser.window_handles[0])
# browser.switch_to.window(browser.window_handles[0])
# #浏览python页面
# browser.get('https://python.org')

#-------------------------------------

# #异常处理
#
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException,NoSuchAttributeException
#
# browser = webdriver.Chrome()
# try:#尝试访问页面
#     browser.get('https://www.taobao.com')
# except TimeoutException:#如果页面响应超时，打印'Time out'
#     print('Time out')
# try:#尝试获取元素
#     browser.find_element_by_id('Hello')
# except NoSuchAttributeException:#如果没能找到元素，打印'No Element'
#     print('No Element')
# finally:#最后关闭页面
#     browser.close()