import scrapy


class LinkedinUser(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    company = scrapy.Field()
    pic = scrapy.Field()
    link = scrapy.Field()
