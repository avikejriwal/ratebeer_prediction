#Returns a list of webpages for a single state

from __future__ import print_function, division
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#This script uses selenium to extract links for beer reviews from ratebeer.com
#then scrape the individual pages for data

def search_state(select_state):
    url = "https://www.ratebeer.com"

    chromedriver = "C:/.../chromedriver" #directory w/ Selenium chromedriver

    driver = webdriver.Chrome(chromedriver)
    driver.get("https://www.ratebeer.com/search.php")

    country  = driver.find_element_by_xpath('//*[@id="CountryID"]')
    country.send_keys('United States')

    state = driver.find_element_by_xpath('//*[@id="StateID"]')
    state.send_keys(select_state)

    most_rated = driver.find_element_by_xpath('//*[@id="SortBy"]')
    most_rated.click()

    submit = driver.find_element_by_xpath('//*[@id="submit1"]')
    submit.click()

    soup = BeautifulSoup(driver.page_source, "lxml")

    data = [x.find_all('tr') for x in soup.find_all('tbody')]

    links = []

    for i, line in enumerate(data[2]):
        link = line.find_all('a',href=True)
        if link:
            links.append(url + link[1]['href'])

    driver.close()

    return links
