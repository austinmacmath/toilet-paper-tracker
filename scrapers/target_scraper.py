from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep

import datetime
import logging
import mysql.connector
import os

def main():
    logging.basicConfig(level=logging.INFO, filename="scraper.log") 
    logger = logging.getLogger()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=os.getenv('MYSQL_PASSWORD'),
        database="tp",
        auth_plugin="mysql_native_password"
    )

    url = "https://www.target.com/c/tissue-toilet-paper-household-essentials/-/N-5xsyk"
    # url = "https://www.costco.com/CatalogSearch?dept=All&keyword=toilet+paper"
    # url = "https://www.cvs.com/shop/household-grocery/paper-plastic-products/bath-tissue"
    # url = "https://www.walmart.com/search/?cat_id=0&grid=true&query=toilet+paper"

    options = Options()
    #options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(url)

    sleep(10)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    logger.info(soup.prettify(), exc_info = True)
    tp_cards = soup.find_all("li", class_="Col-favj32-0 bZxgbc h-padding-a-none h-display-flex")
    for card in tp_cards:
        try:
            brand = card.find("a", class_ = "Link-sc-1khjl8b-0 styles__StyledBrandLink-e5kry1-11 bbqItU h-text-grayDark h-text-sm h-padding-r-tight").text
        except AttributeError:
            brand = None
        try:
            title = card.find("a", class_ = "Link-sc-1khjl8b-0 styles__StyledTitleLink-e5kry1-5 cPukFm h-display-block h-text-bold h-text-bs").text
        except AttributeError:
            title = None
        try:
            price_description = card.find("span", {"data-test" : "product-price"}).text
            price = price_description[1:price_description.find(" ")]
        except AttributeError:
            price = None
        url = "https://www.target.com" + card.find("a")["href"]
        try:
            rating_description = card.find("div", class_ = "RatingStar-sc-1rfld0x-0 ddpeBN").div.text
            rating = rating_description[:rating_description.find(" ")]
        except AttributeError:
            rating = None
        try:
            availability = card.find("div", class_ = "h-text-sm h-text-red")
            availability = "Check in Store"
        except AttributeError:
            availability = "Available"
        collection_date = datetime.datetime.now().strftime("%Y-%m-%d")
        try:
            count_reviews = card.find("span", class_ = "h-text-xs h-text-grayDark").text
        except AttributeError:
            count_reviews = 0

        mycursor = mydb.cursor()
        sql = "INSERT INTO products (brand, title, price, url, rating, availability, collection_date, count_reviews) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (brand, title, price, url, rating, availability, collection_date, count_reviews)
        mycursor.execute(sql, val)
        mydb.commit()

if __name__ == "__main__":
    main()