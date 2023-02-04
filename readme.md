# CityU CS ACM Online Judge Crawler

This is a web cralwer to crawl questions and personal submissions on CityU CS ACM Online Judge System(Requires school VPN): http://acm.cs.cityu.edu.hk/oj2/index.php/.

CityU CS ACM Online Judge System is for data structures and programming courses CS2334, CS3334 and CS3391.

# Environment

Tested with Python 3.9, should work with higher versions

# Usage

Step 1: Put all files into the same folder

Step 2: In terminal, execute ```pip install -r requirements.txt``` to install all required packages

Step 3: Edit configurations in ```configfile.py```

Step 4: Before crawling, make sure your network environment has access to the online judge

Step 5: Change your directory to the first /crawler/ folder (```cd crawler```)


Step 6: To download your questions, execute ```scrapy crawl questions``` inside the first /crawler/ directory to get your questions (Do not run in the child crawler folder!)


Step 7: To download your submissions, execute ```scrapy crawl solutions``` inside the first /crawler/ directory to get your questions (Do not run in the child crawler folder!)

After execution, your questions and submissions should now be downloaded in ```downloaded_files``` folder

# Commands
You should run all commands in terminal and under first /crawler/ directory.

## Crawl completed questions pdf
```
scrapy crawl questions
```

## Crawl personal best submissions
```
scrapy crawl solutions
```

# Configurations

All configurations are in ```configfile.py```

```
# Config for CityU CS ACM Online Judge Crawler

# Username for login
USERNAME = '51234567'
# Password for login
PASSWORD = 'yourpassword'
# Personal statictics to crawl (set to your own link)
PERSONAL_STATISTICS_URL = 'http://acm.cs.cityu.edu.hk/oj2/index.php/u/56614778'
```