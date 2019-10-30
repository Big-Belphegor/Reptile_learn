from urllib.parse import urlencode
from requests.exceptions import RequestException
from config import *
import requests,json,pymongo

#声明MongoDB
# client = pymongo.MongoClient(MONGO_URL)
# db = client[MONGO_DB]

def get_page_index(offset,keyword):
    data = {
        "aid": "24",
        "app_name":" web_search",
        "offset":offset,
        "format":" json",
        "keyword":keyword,
        "autoload":" true",
        "count":" 20",
        "en_qc":" 1",
        "cur_tab":" 1",
        "from":" search_tab",
        "pd":" synthesis",
        "timestamp":" 1571816585600"
    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(data)
    response = requests.get(url)
    try:
        if response.status_code == 200:
            return response.text
    except RequestException:
        print('请求页面出错')
        return None

def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        #data.keys返回JSON的所有Key
        for item in data.get('data'):
            yield item.get('article_url')
            return

def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('Save to MongoDB Success',result)
        return True
    return False

def main():
    html = get_page_index(0,'宇宙图片')
    for item in parse_page_index(html):
        return item


if __name__ == '__main__':
    main()