from bs4 import BeautifulSoup

import logging
import mysql.connector
import os

def main():
    logging.basicConfig(level=logging.INFO, filename="scraper.log") 
    logger = logging.getLogger()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=os.environ.get('MYSQL_PASSWORD'),
        database="tp",
        auth_plugin="mysql_native_password"
    )

    url = "https://www.feedingamerica.org/find-your-local-foodbank#main-content"

    page = open("foodbanks.html").read()
    page = str(page).replace("<br>", "|")
    soup = BeautifulSoup(page, "html.parser")

    cards = soup.find_all("div", class_ = "results-box")
    for card in cards[1:]:
        name = card.find("p", class_ = "name").text
        info = card.find_all("p")[1].text

        street_break = info.find("|")
        street = info[:street_break]

        city_comma = info.find(",", street_break + 1)
        city = info[street_break + 1: city_comma]

        if "P.O" in city or "p.o" in city:
            street_break = info.find("|", street_break + 1)
            city_comma = info.find(",", street_break + 1)
            city = info[street_break + 1: city_comma]


        state_space = info.find(" ", city_comma + 2)
        state = info[city_comma + 2:state_space]

        zip_break = info.find("|", state_space)
        zip_code = info[state_space + 1:zip_break]

        phone = info[zip_break + 1:]
        website = card.find("p", class_ = "url").a.text

        logger.info("Name: " + name)
        logger.info("Street: " + street)
        logger.info("City: " + city)
        logger.info("State: " + state)
        logger.info("Zip: " + zip_code)
        logger.info("Phone: " + phone)
        logger.info("Website: " + website)
        logger.info("Info: " + info)
        logger.info("\n --- \n")

        mycursor = mydb.cursor()
        SQL = "INSERT INTO food_banks (name, street, city, state, zip, phone, website) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (name, street, city , state, zip_code, phone, website)
        mycursor.execute(SQL, val)
        mydb.commit()

        logger.info("Complete")

if __name__ == "__main__":
    main()