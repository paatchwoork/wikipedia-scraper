import re
import requests
import json
from bs4 import BeautifulSoup

class Scraper: 

    '''DOCTRING'''

    def __init__ (self, 
            base_url: str = "https://country-leaders.onrender.com", 
            country_endpoint: str = "/countries", 
            leaders_endpoint: str = "/leaders", 
            cookies_endpoint: str = "/cookie", 
            status_endpoint: str = "/status",
            leaders_data: list = [],
            cookie: object = None,
            p :int = None):

        #Check if the status code is correct
        print(base_url+status_endpoint)
        status = requests.get(base_url+status_endpoint)
        if status != 200: print(f"Could not reach the website, status code = {status}")
        
        self.base_url = base_url
        self.country_endpoint = country_endpoint
        self.leaders_endpoint = leaders_endpoint
        self.cookies_endpoint = cookies_endpoint
        self.status_endpoint = status_endpoint
        self.leaders_data = leaders_data
        self.cookie = cookie

    def __str__ (self):

        return "Scraper object"

    #Returns a cookie from the cookie endpoint
    def refresh_cookie(self) -> object:
        return requests.get(self.base_url+self.cookies_endpoint).cookies




    #Returns a list of the countries from the countries endpoint
    def get_countries(self) -> list:
        self.cookie = self.refresh_cookie()
        return requests.get(self.base_url+self.country_endpoint, cookies = self.refresh_cookie()).json()





    #Populates the leaders_data list. It's gonna be a list of dictionnaries
    def get_leaders(self, country: str) -> None:
        
        self.leaders_data = requests.get(self.base_url+self.leaders_endpoint, cookies = self.refresh_cookie(), params = {"country" : country}).json()





    def get_first_paragraph(self, wikipedia_url: str) -> str:
        soup = BeautifulSoup(requests.get(wikipedia_url).text, 'html.parser')
        paragraphs = soup.find_all("p")
        for self.p in paragraphs:
            self.p = str(self.p)
            if re.search(r"^<p><b>.*</b>",self.p): 
                return re.sub(r"<[^>]*>", r"", self.p)




    def to_json_file(self, filepath: str) -> None:
        with open(filepath, "w") as outfile:
            for leader in self.leaders_data:
                leader_json = json.dumps(leader, indent = 4)
                outfile.write(leader_json)
            
