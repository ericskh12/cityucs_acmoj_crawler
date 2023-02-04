import scrapy
from selenium import webdriver
import time
from scrapy.utils.project import get_project_settings
from selenium.webdriver.common.by import By

class QuotesSpider(scrapy.Spider):

    name = 'questions'

    def __init__(self):
        settings = get_project_settings()
        self.start_urls = [settings.get('PERSONAL_STATISTICS_URL')]
        self.base_url = settings.get('CITU_OJ_URL')
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory" : settings.get('DOWNLOAD_DIRECTORY')}
        chromeOptions.add_experimental_option("prefs",prefs)
        chromedriver = settings.get('SELENIUM_CHROME_WEB_DRIVER')
        self.driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)

    def parse(self, response):
        css_statement = 'tr.verdict-handle-AC td.number_col a::attr(href)'
        questions = response.css(css_statement).getall()

        for question in questions:
            question_url = self.base_url + question
            self.parseQuestionPage(question_url)

        # for questions_url in response.css('.verdict-handle-AC').getall():
        #     print(questions_url)
        self.driver.quit()

    def parseQuestionPage(self, url):
        self.driver.get(url)
        download_buttons = self.driver.find_elements(By.CLASS_NAME, 'img-link')
        for download_button in download_buttons:
            download_button.click()
            break
        time.sleep(1)