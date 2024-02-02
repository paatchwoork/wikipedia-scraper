import re
import requests
import json
from bs4 import BeautifulSoup

class Scraper: 

    '''
    A Wikipedia Scraper that takes the list of world leaders from country-leaders.onrender.com.
        and scrapes the first paragraphs of their wikipedia page, and adds it to the info list

    ATTRIBUTES
        base_url: str           --> The base url of the API
        country_endpoint: str   --> The list of the countries endpoint
        leaders_endpoint: str   --> The list of the countries leaders endpoint
        cookies_endpoint: str   --> The cookies endpoint
        status_endpoint: str    --> The status endpoint
        leaders_data: list      --> A list that will be populated with the leaders' infos
        cookie: object          --> A cookie object used to access the different endpoints
        p:                      --> Is used internally to return the first wikipedia paragraph
        s:                      --> A Session object used to access the websites
    ''' 

    def __init__ (self, 
            base_url: str = "https://country-leaders.onrender.com", 
            country_endpoint: str = "/countries", 
            leaders_endpoint: str = "/leaders", 
            cookies_endpoint: str = "/cookie", 
            status_endpoint: str = "/status",
            leaders_data: list = [],
            cookie: object = None,
            p: int = None,
            s = None):

        self.base_url = base_url
        self.country_endpoint = country_endpoint
        self.leaders_endpoint = leaders_endpoint
        self.cookies_endpoint = cookies_endpoint
        self.status_endpoint = status_endpoint
        self.leaders_data = leaders_data
        self.cookie = cookie
        self.s = requests.Session()

        try:
            self.s.get(base_url+status_endpoint).status_code
        except:
            print(f"Could not reach the webpage {base_url}.")
            exit(1)

        self.refresh_cookie()


    def __str__ (self):
        return "Scraper object"


    def refresh_cookie(self) -> object:
        '''
        Returns a cookie object from the cookie endpoint.
        Used to access the other endpoints.
        '''
        return self.s.get(self.base_url+self.cookies_endpoint).cookies


    def get_countries(self) -> list:
        '''
        Returns a list of the countries from the countries endpoint.
        '''
        #self.cookie = self.refresh_cookie()
        return self.s.get(self.base_url+self.country_endpoint, cookies = self.refresh_cookie()).json()


    def get_leaders(self, country: str) -> None:
        '''
        Populates the leaders_data attribute with the list of the 
        leaders and all their info of the chosen countryd from the leaders endpoint
        '''
        self.leaders_data = self.s.get(self.base_url+self.leaders_endpoint, cookies = self.refresh_cookie(), params = {"country" : country}).json()


    def get_first_paragraph(self, wikipedia_url: str) -> str:
        '''
        Scrapes wikipedia for the first paragraph of the page.
        Is sure to return the first paragraph if it is a person only.
        '''
        soup = BeautifulSoup(self.s.get(wikipedia_url).text, 'html.parser')
        paragraphs = soup.find_all("p")
        for self.p in paragraphs:
            self.p = str(self.p)
            if re.search(r"^<p><b>.*</b>",self.p):      # Looks for the something in bold that starts the paragraph
                return re.sub(r"<[^>]*>", r"", self.p)  # Cleans the data a bit : removes the HTML tags
