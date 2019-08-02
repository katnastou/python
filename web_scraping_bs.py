###THIS ONLY WORKS INSIDE THIS DIR: /usr/local/bin/python3.4/dist-packages
#https://www.rithmschool.com/blog
import requests
from copy import deepcopy
from bs4 import BeautifulSoup
import csv

response = requests.get("https://www.rithmschool.com/blog")
#print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")
with open("blog_data.csv", "w") as csv_file:
	csv_writer = csv.writer(csv_file)
	csv_writer.writerow(["title","link","date"])
	#print(articles)
	for article in articles:
		a_tag = article.find("a")
		title = a_tag.get_text()
		url = a_tag['href']
		date = article.find("time")["datetime"]
		#print (title,url,date)
		csv_writer.writerow([title,url,date])
	

