#前提条件：
# pip install beautifulsoup4
# pip install lxml

from bs4 import BeautifulSoup

html = '''
<head>
    <meta charset="utf8" version='1'/>
    <title>京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=yes"/>
        <div id="search">
                <div class="search-m">
                    <div class="search_logo">
                        <a href="//www.jd.com" class="search_logo_lk" clstag="h|keycount|head|logo_01" tabindex="-1">京东，多快好省</a>
                    </div>

                    <div class="form" role="serachbox">
                        <ul id="shelper" class="search-helper" style="display: none"></ul>
                        <input clstag="h|keycount|head|search_c" type="text"
                               onkeydown="javascript:if(event.keyCode==13) search('key');" autocomplete="off" id="key"
                               accesskey="s"
                               class="text"
                               aria-label="搜索"/>
                        <button clstag="h|keycount|head|search_a" onclick="search('key');return false;" class="button" aria-label="搜索">
                            <i
                                    class="iconfont">&#xe60b;</i></button>
                    </div>
'''
soup = BeautifulSoup(html,'lxml')
# #自动补全代码
# print(soup.prettify())
# #获取代码中的title段
# print(soup.title.string)
# #获取代码中的head段
# print(soup.head)
# #嵌套选择
# print(soup.head.title)
