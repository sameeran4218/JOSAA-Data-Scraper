# JOSAA Data Scraper

## Project Description

This project aims to scrape JOSAA (Joint Seat Allocation Authority) data, extracting information such as the institute name, round, year, branch, gender, quota, seat type, opening rank, and closing rank based on user input. The project utilizes Selenium to interact with the JOSAA website and BeautifulSoup to scrape the necessary data. The extracted data is then organized into a Pandas DataFrame and saved to a CSV file for further analysis.

## Tech Stack

- **Python**: The programming language used for scripting.
- **Selenium**: A web automation tool used to interact with the JOSAA website and fill out the form with user-provided details.
- **BeautifulSoup**: A library for parsing HTML and XML documents, used here for web scraping.
- **Pandas**: A data manipulation and analysis library, used to create a DataFrame from the scraped data and save it to a CSV file.
- **Webdriver**: The specific Selenium WebDriver used to automate web browser interaction. (Chrome Webdriver is used, provided in the reposirtory files)

## Conclusion

This JOSAA Data Scraper project is an efficient tool for extracting and organizing crucial seat allocation data from the JOSAA website based on user inputs. By leveraging the power of Selenium, BeautifulSoup, and Pandas, this script automates the process of data collection and ensures the data is saved in a structured format for easy analysis and further use.

Feel free to contribute to this project by submitting issues or pull requests on our [GitHub repository](https://github.com/yourusername/josaa-data-scraper). Happy scraping!
