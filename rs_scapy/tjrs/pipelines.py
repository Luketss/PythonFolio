# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TjrsPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        # print(adapter.get('dados'))s
        # with open('result.txt', 'a') as f:
        #     for value in item:
        #         f.write(item)
        return item
