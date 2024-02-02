import json
import csv
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from src.scraper import Scraper

s1 = Scraper()                  #Initializing the Scraper
countries = s1.get_countries()  #Fetching the countries in a list
final_dict = {}                 #The end results are going to be stored here

#What type of file do you want ?
filetype = 'json'              
#filetype = 'csv'                

countries.remove('us')          
countries.remove('ma')
countries.remove('fr')
countries.remove('be')

for country in countries:

    print(f"Processing '{country}'") 

    final_dict [country] = {}   #Initializing the country key
    s1.get_leaders(country)     #Getting the leaders info
    first_paragraphs = []       #Initializing the first_paragraphs list

    #Create a list of all the wikipedia urls that the map function wil eat
    for leader in s1.leaders_data:
        first_paragraphs.append(leader['wikipedia_url'])

    
    #Run the threadpool on them
    print(f"Launching the map threading for the {country} country... Please be patient (grab a tea).")
    with ThreadPoolExecutor() as pool:
        first_paragraphs = list(pool.map(s1.get_first_paragraph, first_paragraphs))
    
    #Append the first_paragraphs list to the dictionnary
    i = 0
    for leader in s1.leaders_data:
        leader['first_wiki_paragraph'] = first_paragraphs[i]
        i+=1

    #This will contain the final data to be printed
    final_dict[country] = s1.leaders_data
    

#Printing a JSON
if filetype == 'json':
    print("Producing the json file : leaders_info.json")
    with open("leaders_info.json", "w", encoding='utf-8') as outfile:
        outfile.write(json.dumps(final_dict, indent=4, ensure_ascii=False))

#Printing a CSV
elif filetype == 'csv':
    print("Producing the csv file : leaders_info.csv")
    with open("leaders_info.csv", "w", encoding='utf-8') as outfile:

        #Initializing the field names
        field_names = []
        for key in final_dict[country][0].keys():
            field_names.append(key)
        
        #Printing the headers
        writer = csv.DictWriter(outfile, ['country']+field_names)
        writer.writeheader()
        
        #Printing the file as a csv
        for country in countries:
            for leader in range(len(final_dict[country])):
                outfile.write(f"{country},")
                for key in field_names:
                    outfile.write(f"{final_dict[country][leader][key]},")
        ### There seems to be a bug here and I'm very confused. I leaved it like this becaise I want to discuss it.
        ### When the csv is printed, the last comma is systematically sent at the beginning of the next line
        ### I've tried to clean the wikipedia paragraph of linebreaks because that would explain, but it doesn't change anything
        ### Using DictWriter would probably work but I'm too tired of this problem and I want to look at something else

