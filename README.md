Web Scraping Business in Germany

    This script uses Selenium and the csv library to scrape data on businesses in Germany from the German business directory, "gelbeseiten.de". 
    The script is set up to search for "restaurants" in "Berlin" by default, but the search term and city can easily be modified to suit the user's needs. 
    The scraped data includes the business name, address, postcode, and phone number, and is saved to a csv file named "data.csv".


Requirements

    Python 3
    Selenium library
    chrome driver

Installation
    pip install selenium

You also need to download chrome driver from the official website and add the path to the driver in the script.

Running the script
    python script.py


Configuration
    The script allows you to specify the search term and city by modifying the following lines of code in the script:
    search_term = 'restaurants'
    city = 'berlin'
    You can replace "restaurants" with any business you want to search for and "berlin" with any city in Germany

Output
    The output of the script is a csv file named "data.csv" that contains the following columns:

    title: the name of the business
    street: the street address of the business
    postcode: the postcode of the business
    phone: the phone number of the business
    
Limitations

    The script is set to scrape only from gelbeseiten.de, if you want to scrape other websites you need to adjust the script accordingly
    
    
    Please note that this script is webscraping and some websites may be against it, 
    so it's important to review terms of service of the website before scraping.
    
License

    This project is licensed under the MIT License - see the LICENSE file for details
    
Disclaimer

    Please note that web scraping may be against the terms of service of the website being scraped. 
    It is the responsibility of the user to check if scraping is allowed before using this script. 
    The script provided is for demonstration purposes only and should not be used for any illegal or unauthorized activity. 
    Use this script at your own risk.

    By using this script, you confirm that you will not use it for any unauthorized or illegal activity and will comply with all applicable laws, 
    regulations and terms of service of the website.
    
Contact

    If you have any questions or issues, please feel free to contact me at zorusch.foroutan(at)protonmail(dot)com
    
    
