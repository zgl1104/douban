from scrapy.spiders import CrawlSpider


class Douban(CrawlSpider):
    name = 'doubanTest'
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        print(response.body)
