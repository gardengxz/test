# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class TencentspiderPipeline:
    def process_item(self, item, spider):
        with open('tencent.json','ab') as f:
            data = json.dumps(dict(item), ensure_ascii=False)+'\n'
            f.write(data.encode('utf-8'))
        return item
