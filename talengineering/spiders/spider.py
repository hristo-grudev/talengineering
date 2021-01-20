import re

import scrapy

from scrapy.loader import ItemLoader
from w3lib.html import remove_tags

from ..items import TalengineeringItem


class TalengineeringSpider(scrapy.Spider):
	name = 'talengineering'
	start_urls = [
		'https://talengineering.com/interview-with-arch-eng-klimentin-chernev-young-professionals-must-understand-the-language-of-architects-and-engineers/',
		'https://talengineering.com/bg/interview-with-arch-eng-klimentin-chernev-young-professionals-must-understand-the-language-of-architects-and-engineers/'
	]

	def parse(self, response):
		yield self.parse_post(response)

		pagination_links = response.xpath('//ul[@class="pagination2"]/li/a[@rel="prev"]/@href')
		yield from response.follow_all(pagination_links, self.parse)

	@staticmethod
	def parse_post(response):
		title = response.xpath('//h1[@class="entry-title"]/text()').get().strip()
		description = response.xpath('//div[@class="inner-text"]/p/descendant-or-self::*/text()').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		lang = response.xpath('//html/@lang').getall()
		lang = lang[0][:2]

		item = ItemLoader(item=TalengineeringItem(), response=response)
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('language', lang)

		return item.load_item()
