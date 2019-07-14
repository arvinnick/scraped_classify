import scrapy
from scrapy.crawler import CrawlerProcess
import requests
queries = ['bee','fox','cat','dog','human','rhino']#Any requests could be placed.
class GetImages(scrapy.Spider):
       name = 'DataGain'
       def start_requests(self):
              for n_p in range(90):#number of results pages.
                     for q in queries:
                            yield scrapy.Request( url = 'https://pixabay.com/photos/search/'+q+'/?pagi='+str(n_p+1),#The used website is pixabay.com; but any search engine or database website could be used (obtaining premission from the relevant owners is the users responsiblity)
                                                 callback = self.parse )
       def parse(self,response):
              element = response.css(' img::attr(data-lazy)')#This could be changed based on the used website.
              links = element.extract()
              d=0
              for link in links:
                     n = response.url.find('?')
                     q = response.url[34:n-1]#This could be changed based on the used website.
                     p = response.url[-2:]#This could be changed based on the used website.
                     d = d+1
                     pic = requests.get(url=link).content
                     with open('/path_to_destanation_folder'+q+p+str(d)+'.jpg',
                               mode='wb') as file:
                            file.write(pic)
              
              

process = CrawlerProcess()
process.crawl(GetImages)
process.start()       