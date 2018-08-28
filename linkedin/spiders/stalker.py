# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy import Request
from scrapy.spiders import Spider

from linkedin.spiders.selenium import SeleniumSpiderMixin, extracts_see_all_url, extracts_linkedin_users, \
    get_by_xpath_or_none, wait_invisibility_xpath, extract_company

"""
Number of seconds to wait checking if the page is a "No Result" type.
"""
NO_RESULT_WAIT_TIMEOUT = 3

URLS_FILE = "stalk.txt"

class Stalker(SeleniumSpiderMixin, CrawlSpider):
    name = "stalker"
    allowed_domains = ['www.linkedin.com']

    with open(URLS_FILE, "rt") as f:
        start_urls = [url.strip() for url in f]

    rules = (
        # Extract links matching a single user
        Rule(LinkExtractor(allow=('https:\/\/.*\/in\/.*',), deny=('https:\/\/.*\/in\/edit\/.*',)),
             ),
    )
