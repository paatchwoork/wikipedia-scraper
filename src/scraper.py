class Scraper: 

    '''DOCTRING'''

    def __init__ (self, 
            base_url: str, 
            country_endpoint: str, 
            leaders_endpoint: str, 
            cookies_endpoint: str, 
            leaders_data: dict, 
            cookie: object):
        
        self.base_url = "https://country-leaders.onrender.com"
        self.country_endpoint = "/country"
        self.leaders_endpoint = "/leaders"
        self.cookies_endpoint = "/cookies"
        leaders_endpoint = {}

    def __str__ (self):
        print(f"Check out my Scraper dude. This one is calle {self}!")

    def refresh_cookie(self) -> object:
        pass

    def get_countries(self) -> list:
        pass

    def get_leaders(self, country: str) -> None:
        pass

    def get_first_paragraph(self, wikipedia_url: str) -> str:
        pass

    def to_json_file(self, filepath: str) -> None:
        pass
