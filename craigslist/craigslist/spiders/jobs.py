# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ["craigslist.org"]
    start_urls = ['http://https://newyork.craigslist.org/search/egr/']

    def parse(self, response):
        # response gets the whole html source code & xpath extracts portions of text based on set rules. 
        # //  means instead of starting from the (entire text of html)<html>, just start from the tag that I will specify after it.
        # /a  refers to the <a> tag.
        # [@class="result-title hdrlnk"]  that comes after /a means the <a> tag must have this class name in it.
        # text()  refers to the text of the  <a> tag, which is ”job title”(.i.e. "senior dev").
        #extract() : extract every instance on the web page that follows the same XPath rule into a [list](i.e. a list of job titles)
        titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
        #for loop to yield one title per time in a form of dictionary.
        for title in titles:
            yield {'Title': title}
#You can now run your spider and store the output data into CSV, JSON or XML. To store the data into CSV,
#run the following command in Terminal: (scrapy crawl jobs -o result-titles.csv). 
#The result will be a CSV file:  result-titles.csv in your Scrapy spider directory.



          


