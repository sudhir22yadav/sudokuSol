import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common import keys


browser = webdriver.Chrome()
browser.get('https://www.websudoku.com/?level=1')
browser.find_elements_by_tag_name('tbody')


browser.find_elements_by_xpath('//*[@id=\"puzzle_grid\"]')




'''
url = 'https://www.nine.websudoku.com/?level=1&set_id=2592005782'

header = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
        (KHTML, like Gecko) Ubuntu Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36'}

page = requests.get(url, headers= header)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
'''
