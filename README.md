## RateBeer predictions

In this project I designed a linear model to predict average ratings (out of 5) for beers on RateBeer.com.  

Data was scraped from the website using BeautifulSoup and Selenium.

`scraper.py`: extracts all the necessary information from a ratebeer.com page for a single beers

`searcher.py`: extracts links from RateBeer's search function to run the scraper on

`collect.py`: runs the searcher and scraper to collect data for beers in the United States

data for the 50 states is cleaned and  analyzed in the `analyze.ipynb` notebook
