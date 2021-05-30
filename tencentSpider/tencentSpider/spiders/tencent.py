import scrapy
import json
import time
from tencentSpider.items import TencentspiderItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    # start_urls = ['http://hr.tencent.com/']
    # start_urls = ["https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={}&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=Python&pageIndex=1&pageSize=20&language=zh-cn&area=cn".format(int(time.time())*1000)]
    start_urls = []
    for i in range(1,177):
        url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={}&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=Python&pageIndex=".format(int(time.time()*1000))
        url += str(i) + "&pageSize=10&language=zh-cn&area=cn"
        start_urls.append(url)



    def parse(self, response):
        
        resp = json.loads(response.text)['Data']['Posts']
        for r in resp:
            item = TencentspiderItem()
            item["positienName"] = r["RecruitPostName"]
            item["positienLink"] = r["PostURL"]
            item["positienType"] = r["CategoryName"]
            item["positienAddr"] = r["CountryName"] + '-' + r["LocationName"]
            item["positienIntroduce"] = r["Responsibility"]
            yield item
