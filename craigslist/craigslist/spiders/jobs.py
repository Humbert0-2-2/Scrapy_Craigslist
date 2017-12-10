# -*- coding: utf-8 -*-
import scrapy

        # response gets the whole html source code & xpath extracts portions of text based on set rules. 
        # //  means instead of starting from the (entire text of html)<html>, just start from the tag that I will specify after it.
        # /a  refers to the <a> tag.
        # [@class=" "]  that comes after /a means the <a> tag must have this class name in it.
        # text()  refers to the text of the  <a> tag, which is ”job title”(.i.e. "senior dev").
        #extract() : extract every instance on the web page that follows the same XPath rule into a [list](i.e. a list of job titles)
        #Note that here you will not use extract() because it is the wrapper from which you will extract other HTML nodes.


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ["craigslist.org"]
    start_urls = [https://seattle.craigslist.org/search/tac/jjj']
  def parse(self, response):
        Jobs = response.xpath('//p[@class="result-info"]')
      
       for job in jobs:
        title = job.xpath('a/text()').extract_first()
        #or title = job.xpath('.//a/text()').extract_first(), title”. Without any slashes, because it complements or depends on the XPath expression of the job wrappe
        #You can extract the job address and URL from the wrappers using the same for loop as follows:
        address = job.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').extract_first("")[2:-1]
        relative_url = job.xpath('a/@href').extract_first()
        absolute_url = response.urljoin(relative_url)
        
        yield{'URL':absolute_url, 'Title':title, 'Address':address}
                 
                  
                  

        
      
#You can now run your spider and store the output data into CSV, JSON or XML. To store the data into CSV,
#run the following command in Terminal: (scrapy crawl jobs -o result-titles.csv). 
#The result will be a CSV file:  result-titles.csv in your Scrapy spider directory.

#if you want to scrape several details about each job, you will not extract them separately, 
#you scrape the whole “container” or “wrapper” of each job including all the information you need, 
#and then extract pieces of information from each container/wrapper.
        



          


