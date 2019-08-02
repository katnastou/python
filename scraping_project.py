# -*- coding: utf-8 -*-
"""
Created on Sun Jan 06 13:10:32 2019

@author: Infinity
"""
import requests
from random import choice
from bs4 import BeautifulSoup
import csv
BASE_URL = "http://quotes.toscrape.com"

def start_game(quotes):
    quote = choice(quotes)
    print(quote["text"])
    print(quote["author"])
    remaining_guesses = 4
    guess=''
    while guess.lower() != quote["author"].lower() and remaining_guesses>0:
        guess = input("Who said this quote? Guesses remaining: {}\n".format(remaining_guesses))
        if guess.lower() == quote["author"].lower():
            print("You got it right")
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            res = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(res.text,"html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint: The author was born on {birth_date} in {birth_place}")
        elif remaining_guesses == 2:
            print(f"Here's a hint: The author's first name starts with: {quote['author'][0]}")
        elif remaining_guesses == 1:
            last_initial = quote['author'].split(" ")[1][0]
            print(f"Here's a hint: The author's last name starts with: {last_initial}")
        else:
            print(f"Sorry you run out of guesses. The answer is {quote['author']}")
    
    again = ''
    again = input("Would you like to play again (y/n)?")
    
    while again not in ('y','yes', 'n', 'no'):
        again = input("Would you like to play again (y/n)?")
    if again.lower() in ('y','yes'):
        return start_game(quotes)
    else:
        print ("ok, goodbye!")
        
quotes = scrape_quotes()
start_game(quotes)
#print("AFTER WHILE LOOP")
    
#with open("blog_data.csv", "wb", newline='') as csv_file: #newline ='' windows only
#	csv_writer = csv.writer(csv_file)
#	csv_writer.writerow(["title","link","date"])
	#print(articles)
#	for article in articles:
#		a_tag = article.find("a")
#		title = a_tag.get_text()
#		url = a_tag['href']
#		date = article.find("time")["datetime"]
		#print (title,url,date)
#		csv_writer.writerow([title,url,date])
	