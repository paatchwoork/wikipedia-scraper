import json
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import re
from src.scraper import Scraper
from bs4 import BeautifulSoup
import requests

s1 = Scraper()
countries = s1.get_countries()
print(countries)
leader_json = {}
for country in countries:
    leader_json[country] = {}


#US TESTING 
country = 'us' 
print(f"Processing {country}") 
s1.get_leaders(country) 
first_paragraphs = []
for leader in s1.leaders_data:
    leader_name = leader ['first_name'] + " " + leader ['last_name']
    #Create a list of all the wikipedia urls
    first_paragraphs.append(leader['wikipedia_url'])

#run the threadpool on them
print(f"Launching the map threading for the {country} country... Please be patient (grab a tea).")
with ThreadPoolExecutor() as pool:
    first_paragraphs = list(pool.map(s1.get_first_paragraph, first_paragraphs))

#Append the first_paragraphs list to the dictionnary
i = 0
for leader in s1.leaders_data:
    leader['first_wiki_paragraph'] = first_paragraphs[i]
    i+=1

print("Producing the json file.")
with open("sample.json", "w") as outfile:
    outfile.write(json.dumps(s1.leaders_data, indent=4))
