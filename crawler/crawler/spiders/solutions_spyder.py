import scrapy
from selenium import webdriver
import time
from scrapy.utils.project import get_project_settings
import os

class QuotesSpider(scrapy.Spider):
    name = "solutions"

    def __init__(self):
        settings = get_project_settings()
        self.start_urls = [settings.get('PERSONAL_STATISTICS_URL')]
        self.username = settings.get('USERNAME')
        self.password = settings.get('PASSWORD')
        self.login_url = settings.get('CITYU_OJ_LOGIN_URL')
        self.submission_url = settings.get('CITYU_OJ_SUBMISSION_URL')
        self.download_directory = settings.get('DOWNLOAD_DIRECTORY')

        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory" : self.download_directory}
        chromeOptions.add_experimental_option("prefs",prefs)
        chromedriver = settings.get('SELENIUM_CHROME_WEB_DRIVER')
        self.driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)

    def parse(self, response):
        self.driver.get(self.login_url)
        username = self.driver.find_element_by_name('logon[contact]')
        password = self.driver.find_element_by_name('logon[password]')
        loginbutton = self.driver.find_element_by_class_name('button-confirm')
        username.send_keys(self.username)
        password.send_keys(self.password)
        loginbutton.click()
        
        css_statement = 'tr.verdict-handle-AC td.sid_col a::text'
        submissions = response.css(css_statement).getall()
        css_statement = 'tr.verdict-handle-AC td.number_col a::text'
        questions_number = response.css(css_statement).getall()
        submission_url = self.submission_url
        txt = '.txt'
        cpp = '.cpp'
        print(len(submissions))

        for question_number, submission in zip(questions_number, submissions):
            url = submission_url + submission + txt
            self.driver.get(url)
            tag = self.driver.find_elements_by_tag_name('pre')
            filename = os.path.join(self.download_directory,question_number+cpp)
            for t in tag:
                with open(filename, 'w') as f:
                    f.write(t.text)
                break
            time.sleep(1)
        
        self.driver.quit()