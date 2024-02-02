# Wikipedia world leader scraper
## By Léa Konincks

This little script will use a Scraper object to retrieve data from a world leaders list and use that data to retrieve the first wikipedia paragraph.\
It adds the wikipedia paragraph to the total info and prints it to a .json file.\
You can change the file type to .csv by commenting the line 12 and uncommenting the line 13 in the main.py file. This feature has a known bug that I left in the code for educational reasons (I want to understand).

The program runs by itself and will print the file at the end.

Multithreading is used to retrieve the data off Wikipedia in the fastest way possible.

To run the code, simply type ```python main.py``` in your terminal.

All the python packages needed are listed in the wikiscrap.yml file.\
To install them into you virtual environment, use ```conda env create -f wikiscrap.yml```

### Have fun <3 ~ Léa
