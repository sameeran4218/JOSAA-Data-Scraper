A JOSAA data scraper which extracts the opening and closing ranks for each gender based on the ser input of year, round number, institute type and institute name.
We implement Selenium to interact with the form and enter details provided by the user
We then use BeautifulSoup to scrape all the necessary data from the webpage like institute,gender,opening rank and closing rank
Finally we use Pandas to create a dataframe of the extracted data and save it to a csv file
