"""
爬取豆瓣250榜单的电影，并对其进行初步的分析
"""


from lxml import etree
import requests
from requests.exceptions import RequestException
import csv
from multiprocessing import Pool

class Douban_top_250():
    def __init__(self):
        self.url = 'https://movie.douban.com/top250?start='


    def get_first_page(self, url):
        try:
            resp = requests.get(url)
            if resp.status_code == 200:
                return resp.text
            return None
        except RequestException:
            return None


    def parse_one_page(self, html):
        pages = etree.HTML(html)
        # print(bf)
        items = pages.xpath('//ol[@class="grid_view"]/li')
        # print(items)
        for item in items:
            # print(movie)
            content = item.xpath('./div/div[2]/div[2]/p[1]//text()')
            director_actor = content[0].strip().split("\xa0\xa0\xa0")
            year_country_type = content[1].strip().split("\xa0/\xa0")
            ac_link = item.xpath('./div/div[2]/div[1]/a/@href')[0]
            yield {
                'index' : item.xpath('./div/div/em/text()')[0],
                'title' : item.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0],
                'score' : item.xpath('div/div[2]/div[2]/div/span[2]/text()')[0],
                'director' : director_actor[0].split(" ")[1],
                'year' : year_country_type[0],
                'country' : year_country_type[1],
                'style' : year_country_type[2],
                'actors' : ','.join(self.get_link(ac_link)),
            }


    def get_link(self, url):
        resp = requests.get(url)
        page = etree.HTML(resp.text)
        actor = page.xpath('//*[@class="actor"]/span[2]//text()')[::2]
        return actor


    def write_to_file(self, content):
        with open('movie_top_250.csv', 'a+', encoding='utf-8', newline='') as f:
            fieldnames = ['index', 'title', 'score', 'director', 'year', 'country', 'style', 'actors']
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writerow(content)


    def main(self, offset):
        url = self.url + str(offset) + "&filter="
        html = self.get_first_page(url)
        for item in self.parse_one_page(html):
            self.write_to_file(item)


if __name__ == '__main__':
    a = Douban_top_250()
    for i in range(10):
        print(f'正在爬取第{i+1}页数据:')
        page_num = i * 25
        a.main(page_num)