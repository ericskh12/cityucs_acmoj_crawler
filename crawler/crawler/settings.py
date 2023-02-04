import os
import sys
sys.path.append("..") # Adds higher directory to python modules path.

import configfile

# Username for login
USERNAME = configfile.USERNAME
# Password for login
PASSWORD = configfile.PASSWORD
# Personal statictics to crawl
PERSONAL_STATISTICS_URL = configfile.PERSONAL_STATISTICS_URL

# Directory to place downloaded files
DOWNLOAD_DIRECTORY = os.path.join(os.path.dirname(os.getcwd()), 'downloaded_files')

# URL used for the crawler
# Shouldn't modify anything here if the url of Cityu Online Judge doesn't change
CITU_OJ_URL = 'http://acm.cs.cityu.edu.hk'
CITYU_OJ_LOGIN_URL = 'http://acm.cs.cityu.edu.hk/oj2/index.php/account/login'
CITYU_OJ_SUBMISSION_URL = 'http://acm.cs.cityu.edu.hk/oj2/index.php/submission/'

# Scrapy settings for crawler project

BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
