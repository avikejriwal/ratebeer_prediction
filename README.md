## RateBeer predictions

In this project I designed a linear model to predict average ratings (out of 5) for beers on [RateBeer](https://www.ratebeer.com/).  

### Requirements

pandas, requests, patsy, beautifulsoup4, selenium with [chromedriver](https://chromedriver.storage.googleapis.com/index.html?path=2.30/), jupyter notebook, scikit-learn

### Details

Data was scraped from the website using BeautifulSoup and Selenium.

`scraper.py`: extracts all the necessary information from a ratebeer.com page for a single beers

`searcher.py`: extracts links from RateBeer's search function to run the scraper on

`collect.py`: runs the searcher and scraper to collect data for beers in the United States

data for the 50 states is cleaned and  analyzed in `analyze.ipynb`

`beer_model.pkl`: contains a trained Ridge model.

### Results

ABV and Calories are highly correlated, so I dropped the latter when building the model.

Average testing performance falls in the range of 0.63 to 0.66 for r<sup>2</sup>, with a residual standard deviation of 0.25-0.27.

Most important features:
- ABV
- State of origin
- Beer style

### [Read More](https://avikejriwal.github.io/Beer-Rating-Regression-Model/)
