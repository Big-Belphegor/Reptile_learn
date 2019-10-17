# 前提条件：pip install pyquery
# 官方文档：https://pythonhosted.org/pyquery/api.html

# #字符串初始化
# html = '''
# <div>
#   <ul>
#     <li class='item-0'>frist item</li>
#     <li class='item-1'><a href="link2.html">second item</a></li>
#     <li class='item-0 active'><a href="link3.html"><span class="bold">third item</span></a></li>
#     <li class='item-1 active'><a href="link4.html">fourth item</a></li>
#     <li class='item-0'><a href="link5.html">fifth item</a></li>
#   </ul>
# </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# print(doc('li'))

# #URL初始化
# from pyquery import PyQuery as pq
# doc = pq(url='http://www.baidu.com')
# print(doc('head'))

# #文件初始化
# from pyquery import PyQuery as pq
# doc = pq(filename='/path/file')
# print(doc('xxx'))

#---------------------------------------------

#查找元素
# html = '''
# <div>
#   <ul class='list'>
#     <li class='item-0'>frist item</li>
#     <li class='item-1'><a href="link2.html">second item</a></li>
#     <li class='item-0 active'><a href="link3.html"><span class="bold">third item</span></a></li>
#     <li class='item-1 active'><a href="link4.html">fourth item</a></li>
#     <li class='item-0'><a href="link5.html">fifth item</a></li>
#   </ul>
# </div>
# '''

# #查找任意元素
# from pyquery import PyQuery as pq
# #--首先初始化，查询list类下的标签
# doc = pq(html)
# ltems = doc('.list')
# print(type(ltems))
# print(ltems)
# #--然后对生成的实例进行查找操作
# #--查找'li'标签
# lis = ltems.find('li')
# #--查找'li'下的'a'标签
# lis2 = ltems.find('li').find('a')
# print(type(lis))
# print(lis)
# print(lis2)

# #查找子元素
# #--查找ltems的子元素中包含active的标签
# lis3 = ltems.children('.active')
# print(lis3)

#---------------------------------------------

# #父元素
# html = '''
# <div id='container'>
#   <ul class='list'>
#     <li class='item-0'>frist item</li>
#     <li class='item-1'><a href="link2.html">second item</a></li>
#     <li class='item-0 active'><a href="link3.html"><span class="bold">third item</span></a></li>
#     <li class='item-1 active'><a href="link4.html">fourth item</a></li>
#     <li class='item-0'><a href="link5.html">fifth item</a></li>
#   </ul>
# </div>
# '''

# from pyquery import PyQuery as pq
# doc = pq(html)
# ltems = doc('.list')
# #指定查找为父元素标签
# container = ltems.parent()
# print(type(container))
# print(container)

#---------------------------------------------

# #兄弟元素
# html = '''
# <div class='wrap'>
# <div id='container'>
#   <ul class='list'>
#     <li class='item-0'>frist item</li>
#     <li class='item-1'><a href="link2.html">second item</a></li>
#     <li class='item-0 active'><a href="link3.html"><span class="bold">third item</span></a></li>
#     <li class='item-1 active'><a href="link4.html">fourth item</a></li>
#     <li class='item-0'><a href="link5.html">fifth item</a></li>
#   </ul>
# </div>
# '''
#
# from pyquery import  PyQuery as pq
# doc = pq(html)
# #含义：'.list'查找类为'list'的标签，后面的空格代表继续查找其下的标签，'.time-0.active'查找’类包含'item-0'及'active'的'li'标签。
# li = doc('.list .item-0.active')
# #打印匹配信息，发现只会有一行匹配
# print(li)
# #查询兄弟元素，类似模糊查询，会打印类似的元素
# print(li.siblings())
# #也可以从兄弟元素中再次查找指定的信息
# print(li.siblings('.active'))

#---------------------------------------------

# #元素的遍历
# html = '''
# <div class='wrap'>
# <div id='container'>
#   <ul class='list'>
#     <li class='item-0'>frist item</li>
#     <li class='item-1'><a href="link2.html">second item</a></li>
#     <li class='item-0 active'><a href="link3.html"><span class="bold">third item</span></a></li>
#     <li class='item-1 active'><a href="link4.html">fourth item</a></li>
#     <li class='item-0'><a href="link5.html">fifth item</a></li>
#   </ul>
# </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# #'.items()'转换类型为generator
# lis = doc('li').items()
# lis2 = doc('li')
# print(type(lis))
# print(type(lis2))
# for li in lis:
#     print(li)

#---------------------------------------------

# #获取信息

# #获取属性
# html = '''
# <div class='wrap'>
# <div id='container'>
#   <ul class='list'>
#     <li class='item-0'>frist item</li>
#     <li class='item-1'><a href="link2.html">second item</a></li>
#     <li class='item-0 active'><a href="link3.html"><span class="bold">third item</span></a></li>
#     <li class='item-1 active'><a href="link4.html">fourth item</a></li>
#     <li class='item-0'><a href="link5.html">fifth item</a></li>
#   </ul>
# </div>
# '''
#
# from pyquery import PyQuery as pq
# doc = pq(html)
# #首先过滤出想要的标签
# a = doc('.item-0.active a')
# print(a)
# #然后获取属性
# print(a.attr('href'))
# #效果同上
# print(a.attr.href)

# #获取文本
# html = '''
# <div class='wrap'>
# <div id='container'>
#   <ul class='list'>
#     <li class='item-0'>frist item</li>
#     <li class='item-1'><a href="link2.html">second item</a></li>
#     <li class='item-0 active'><a href="link3.html"><span class="bold">third item</span></a></li>
#     <li class='item-1 active'><a href="link4.html">fourth item</a></li>
#     <li class='item-0'><a href="link5.html">fifth item</a></li>
#   </ul>
# </div>
# '''
#
# from pyquery import PyQuery as pq
# doc = pq(html)
# a = doc('.item-0.active a')
# print(a)
# #获取'a'标签内的文字部分
# print(a.text())
# #获取'a'标签内的HTML部分
# print(a.html())

#---------------------------------------------

# #DOM操作
# html = '''
# <div class='wrap'>
# <div id='container'>
#   <ul class='list'>
#     <li class='item-0'>frist item</li>
#     <li class='item-1'><a href="link2.html">second item</a></li>
#     <li class='item-0 active'><a href="link3.html"><span class="bold">third item</span></a></li>
#     <li class='item-1 active'><a href="link4.html">fourth item</a></li>
#     <li class='item-0'><a href="link5.html">fifth item</a></li>
#   </ul>
# </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# #移除属性
# li_2 = li.remove_class('active')
# print(li_2)
# #添加属性
# li_3 = li.add_class('active')
# print(li_3)
# #修改元素属性
# li_4 = li.attr('name','link')
# print(li_4)
# #修改样式属性
# li_5 = li.css('font-size','16px')

# #移除标签
# html = '''
# <div class="test">
#   Hello,world!
#   <p>This is a p</p>
# </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# test = doc('.test')
# #此时会获取到两个内容，假设我们只想要'Hello,world'
# print(test.text())
# #如下操作,删除'p'标签的内容
# test.find('p').remove()
# print(test.text())