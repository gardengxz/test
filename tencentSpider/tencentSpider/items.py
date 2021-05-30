# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    positienName = scrapy.Field()
    positienLink = scrapy.Field()
    positienType = scrapy.Field()
    positienAddr = scrapy.Field()
    positienIntroduce = scrapy.Field()
