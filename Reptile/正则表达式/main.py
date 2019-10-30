#常用匹配，从字符串的起始位置进行匹配(rm.match)
import re
content = 'Hello Alien,welcome in'
result = re.match('^Hello\s.*in$',content)
print(result)
#打印匹配到的字符串
print(result.group())
#打印匹配到的字符串长度
print(result.span())

#泛匹配
import re
content = 'Hello Alien,welcome in'
result = re.match('^Hello.*in$',content)
print(result)

#匹配目标，匹配一个范围
import re
content = 'ABC 123 DEF 456'
result = re.match('^ABC\s(\d+)\s',content)
print(result)

#全局匹配，找寻字符串中所有匹配项(re.findall)
import re
html = '''
                <li class="sn-favorite menu-item">
                    <a href="//shoucang.taobao.com/shop_collect_list.htm" target="_top" rel="nofollow">收藏的店铺</a>
                </li>
                <li class="sn-home">
                    <a href="//www.taobao.com/">淘宝网</a>
                </li>
'''
# results = re.findall('<li.*?>\s*(<a.*>)?(.*)(</a>)?\s*<li>',html,re.S)
results = re.findall('<li.*?>\s*?(<a.*>)(\w+)(</a>)\s*?</li>',html,re.S)
# print(results)
for x in results:
    print(x[1])
#注意：re.S的作用是将多行字符串视为一行

#替换字符串，re.sub用于替换匹配项
import re
content = 'Password: 123456'
a = re.sub('\d+','',content)
print(a)

#复用字符串，备注're.search'用于全局字符串搜索进行匹配，re.compoile是将字符串转化为正则表达式
import re
content = 'Username:Alien Password:123456'
pattern = re.compile('\d+',re.S)
result = re.search(pattern,content)
print(result)