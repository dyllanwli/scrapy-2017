from scrapy.spiders import Spider
from scrapy import Request
from douban.items import DoubanItem

class DoubanTop(Spider):
    name = 'Douban'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    def start_requests(self):
        url = 'https://book.douban.com/top250'
        yield Request(url,headers=self.headers)

    def parse(self, response):
        item = DoubanItem()
        books =  response.xpath('//div[@class="article"]//div//table')
        rank = 0
        for book in books:
            rank += 1
            item.book_name = book.xpath('.//div[@class = "pl2"]/a/text()').extract()[0]
            item.author = book.xpath('.//p[@class = "pl"]//text()').extract()[0]
            item.ranking = str(rank)
            item.score = book.xpath('.//span[@class = "rating_nums"]//text()').extract()[0]
            item.score_num = book.xpath('.//div[@class = "star clearfix"]//span[@class = "pl"]//text()').re(ur'(\d+)人评价')[0]
            yield item