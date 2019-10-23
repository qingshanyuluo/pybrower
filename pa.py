import requests
from lxml import etree
import csv
# import time

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

def get_url(url):
    res = requests.get(url, headers=headers)
    # print(res.text)
    html = etree.HTML(res.text)
    infos = html.xpath('//dl[@class="board-wrapper"]/dd')
    for info in infos:
        # title = info.xpath('div/div/div[1]/p[1]/a/text()')
        title = info.xpath('div/div/div[1]/p[1]/a/text()')[0]
        author = info.xpath('div/div/div[1]/p[2]/text()')[0].strip().strip('主演：')
        publish_time = info.xpath('div/div/div[1]/p[3]/text()')[0].strip('上映时间')
        star_1 = info.xpath('div/div/div[2]/p/i[1]/text()')[0]
        star_2 = info.xpath('div/div/div[2]/p/i[2]/text()')[0]
        star = star_1 + star_2
        movie_url = 'https://maoyan.com' + info.xpath('div/div/div[1]/p[1]/a/@href')[0]
        # print(title, author, publish_time, star)
        get_info(movie_url,title, author, publish_time, star)

def get_info(url,title, author, publish_time, star):
    res = requests.get(url, headers=headers)
    html = etree.HTML(res.text)
    style = html.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/text()')[0]
    movie_time = html.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[2]/text()')[0].split('/')[1].strip().strip('分钟')
    print(title,author,publish_time,star,style,movie_time)
    writer.writerow([title,author,publish_time,star,style,movie_time])


if __name__ == "__main__":
    fp = open('maoyan.csc','w',newline='',encoding='utf-8')
    writer = csv.writer(fp)
    writer.writerow(['title','author','publish_time','star','style','movie_time'])
    urls = ['https://maoyan.com/board/4?offset={}'.format(str(i)) for i in range(0, 100, 10)]
    for url in urls:
    # url = 'https://maoyan.com/board/4'
        get_url(url)
