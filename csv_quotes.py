# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:47:18 2019

@author: Infinity
"""

import requests
from bs4 import BeautifulSoup
#from time import sleep
from csv import DictWriter
BASE_URL = "http://quotes.toscrape.com"


def scrape_quotes():
    all_quotes = []
    url = "/page/1/"
    while url:
        response = requests.get(BASE_URL+url)
        #print("Now scaping {}{}".format(BASE_URL,url))
        #print(response.text)
        soup = BeautifulSoup(response.text.encode('unicode-escape').decode('utf-8'), "html.parser")
        #print(soup.body)
        quotes = soup.find_all(class_="quote")
    
    
        for quote in quotes:
            text = quote.find(class_="text").get_text()
            name = quote.find(class_="author").get_text()
            bio = quote.find("a")["href"] #we want the href from the first anchor tag
            all_quotes.append({
                    "text":text,
                    "author":name,
                    "bio-link": bio})
        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
        #sleep(1)
    return all_quotes

quotes = scrape_quotes()

with open("quotes.csv", "w") as file:
    headers = ["text","author","bio-link"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for quote in quotes:
        csv_writer.writerow(quote)