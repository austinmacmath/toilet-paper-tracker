from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import datetime
import logging
import mysql.connector

def main():
    logging.basicConfig(level=logging.INFO, filename="scraper.log") 
    logger = logging.getLogger()

    url = "https://www.target.com/c/tissue-toilet-paper-household-essentials/-/N-5xsyk"

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    tp_card = soup.find_all("a", class_="product-title-link line-clamp line-clamp-2")
    for brand in brands:
        print(brand['href'])