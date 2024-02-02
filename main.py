import json
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
leaders = s1.leaders_data 
i = 0
for leader in leaders:
    i += 1
    leader_name = leader ['first_name'] + " " + leader ['last_name']
    print(f"processing {leader_name}")
    first_paragraph = s1.get_first_paragraph(leader ['wikipedia_url'])
    leader_json[country][leader_name] = first_paragraph
    if i == 5: break
with open("sample.json", "w") as outfile:
    outfile.write(json.dumps(leader_json, indent=4))
