'''
Created on 2017年8月1日

@author: lenovo
'''

import scrapy.cmdline

if __name__ == '__main__':
    #scrapy.cmdline.execute("scrapy crawl quotes -o quotes.json".split())
    scrapy.cmdline.execute("scrapy crawl author -o author.jl".split())