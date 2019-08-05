import scrapy
from scrapy.crawler import CrawlerProcess
import requests
queries = ['bee','fox','cat','dog','human','rhino']
class GetImages(scrapy.Spider):
       name = 'DataGain'
       def start_requests(self):
              for n_p in range(90):
                     for q in queries:
                            yield scrapy.Request( url = 'https://pixabay.com/photos/search/'+q+'/?pagi='+str(n_p+1), callback = self.parse )
       def parse(self,response):
              element = response.css(' img::attr(data-lazy)')
              links = element.extract()
              d=0
              for link in links:
                     n = response.url.find('?')
                     q = response.url[34:n-1]
                     p = response.url[-2:]
                     d = d+1
                     pic = requests.get(url=link).content
                     with open('/home/mohammad/Documents/bee_image_detector/data/'+q+str(d)+'.jpg',mode='wb') as file:
                            file.write(pic)
              
              

process = CrawlerProcess()
process.crawl(GetImages)
process.start()       