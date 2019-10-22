import requests,re,json
from requests.exceptions import RequestException
from multiprocessing import Pool

def get_page(url):
    #获取要爬取的页面源码
    try:
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200 or response.status_code == 403:
            return response.text
        return None
    except RequestException:
        return None

def parse_page(html):
    #爬取需要的信息
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>'
                         +'.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'Index':item[0],
            'image':item[1],
            'Name':item[2],
            'Actor':item[3].strip()[3:],
            'Time':item[4].strip()[5:],
            'Score':item[5]+item[6]
        }

def write_to_file(itme):
    #存储获取的数据
    with open('film_list','a',encoding='utf-8') as f:
        f.write(json.dumps(itme,ensure_ascii=False) + '\n')
        f.close()

def main(num):
    url = 'https://maoyan.com/board/4?offset=' + str(num)
    html = get_page(url)
    for item in parse_page(html):
        # print(item)
        write_to_file(item)

if __name__ == '__main__':
    #---单进程运行
    # for i in range(10):
    #     main(i*10)
    #---多进程运行，数据提取时需要自行排序
    pool = Pool()
    pool.map(main,[i*10 for i in range(10)])