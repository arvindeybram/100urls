import scrapy,os,sys
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class FollowAllSpider(CrawlSpider):
	name = 'follow_all'
	with open("Testset.txt", "rt") as f:
		start_urls = [url.strip() for url in f.readlines()]
	#start_urls=['https://www.google.co.in/search?q=python+with+open+a+file+in+write+mode&rlz=1C1GCEB_enIN808IN808&oq=python+with+open+a+file+in+write+mode&aqs=chrome..69i57.9960j0j7&sourceid=chrome&ie=UTF-8']
	rules = [Rule(LinkExtractor(), callback='parse_item', follow=True)]
	
	def parse_item(self, response):
	
		MAX_RANGE = 1000
		count=0 
		f = open("Testset.txt",'a+') 
		for href in response.css('a::attr(href)'):
			count+=1
			if count <= MAX_RANGE:
				extracted_url=(str(href)+'\n').replace('<Selector xpath=\'descendant-or-self::a/@href\' data=\'','').replace('\'>','')
				if "https" in extracted_url:
					f.write(extracted_url)
				else:
					pass
			else:
				break
		f.close()
			
				
			