# CityU CS ACM Online Judge Crawler

This is a web cralwer to crawl questions and personal submissions on CityU CS ACM Online Judge System(Requires school VPN): http://acm.cs.cityu.edu.hk/oj2/index.php/.
CityU CS ACM Online Judge System is for data structure and programming courses CS3334 and CS3391.

# Environment

Python 3.8

## Required packages
Scrapy
Selenium
time
os
Chrome webdriver for selenium

# Configurations
```
# Username for login
USERNAME = '51234567'
# Password for login
PASSWORD = '123'
# Personal statictics to crawl (Change to your personal statictics link)
PERSONAL_STATISTICS_URL = 'http://acm.cs.cityu.edu.hk/oj2/index.php/u/56614778'
# Directory to place downloaded files
DOWNLOAD_DIRECTORY = 'C:\\Users\\ABC\\cityucs_acmoj_crawler\\downloaded_files'
# Location of selenium chrome web driver (The version should match your personal chrome browser)
# Download here if you don't have the driver on your system: https://chromedriver.chromium.org/downloads
SELENIUM_CHROME_WEB_DRIVER = 'C:\\Users\\ABC\\git\\cityucs_acmoj_crawler\\chromedriver.exe'

# URL used for the crawler
# Shouldn't modify anything here if the url of Cityu Online Judge doesn't change
CITU_OJ_URL = 'http://acm.cs.cityu.edu.hk'
CITYU_OJ_LOGIN_URL = 'http://acm.cs.cityu.edu.hk/oj2/index.php/account/login'
CITYU_OJ_SUBMISSION_URL = 'http://acm.cs.cityu.edu.hk/oj2/index.php/submission/'
```

# Usage

Step0: Install all required packages and chrome webdriver(There is already one copy in this project, you can modify settings.py to redirect)

Step1: Download the folder

Step2: Edit the configuration settings in crawler/crawler/settings.py

Step3: In terminal,	run scrapy crawl questions in the first /crawler/ directory (Do not run in the child crawler folder!)

Step4: In terminal, run scrapy crawl solutions in the first /crawler/ directory (Do not run in the child crawler folder!)

# Commands
You should run all commands in terminal and under first /crawler/ directory.

##Crawl completed questions pdf
scrapy crawl questions

##Crawl personal best submissions
scrapy crawl solutions
