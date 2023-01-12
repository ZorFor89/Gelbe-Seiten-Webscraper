import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the search term and city to search for
search_term = 'restaurants'
city = 'berlin'

# Open a browser and navigate to the website
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options)

# Construct the search URL
url = 'https://www.gelbeseiten.de'
browser.get(url)

# Wait for the cookies consent box to appear and click the "Accept" button
accept_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.cmpboxbtn.cmpboxbtnyes.cmptxt_btn_yes')))
accept_button.click()

# Find the input fields for the search term and city
search_term_input = browser.find_element(By.ID, 'what_search')
city_input = browser.find_element(By.ID, 'where_search')

# Enter the search term and city into the input fields
search_term_input.send_keys(search_term)
city_input.send_keys(city)

# Find the submit button and click it to initiate the search
submit_button = browser.find_element(By.CSS_SELECTOR, 'button.gc-btn.gc-btn--black.gc-btn--l.search_go')
submit_button.click()

# Wait for the page to load
time.sleep(5)

# Find the element containing the list of items to scrape
elem_list = browser.find_element(By.CSS_SELECTOR, '#teilnehmer_block')

# Set the flag to indicate that the "Next Page" button is not disabled
isNextDisabled = False

# Open the CSV file for writing
csvfile = open('data.csv', 'w', newline='')
fieldnames = ['title', 'street', 'postcode', 'phone']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

# Create a set to store the phone numbers that have been scraped
scraped_phones = set()

# Enter a try block to catch any exceptions that may occur
try:
    while not isNextDisabled:
        # Find the elements to scrape
        items = elem_list.find_elements(By.CSS_SELECTOR, 'article.mod.mod-Treffer')

        for item in items:
            title = item.find_element(By.TAG_NAME, 'h2').text
            street = item.find_element(By.CSS_SELECTOR, 'p[data-wipe-name="Adresse"]').text.split(',')[0]
            postcode = item.find_element(By.CSS_SELECTOR, 'p[data-wipe-name="Adresse"] span.nobr').text

            # Try to find the phone number, and skip this item if it is not found
            try:
                phone = item.find_element(By.CSS_SELECTOR, 'p.mod-AdresseKompakt__phoneNumber').text
            except:
                continue

            # Check if the phone number has already been scraped
            if phone in scraped_phones:
                continue

            # Write the data to the CSV file
            writer.writerow({'title': title, 'street': street, 'postcode': postcode, 'phone': phone})

            # Add the phone number to the set of scraped phones
            scraped_phones.add(phone)

        # Try to click the "Next Page" button
        try:
            next_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.mod-LoadMore--button')))
            next_button.click()
        except Exception as e:
            isNextDisabled = True

except Exception as e:
    print(e)
finally:
    # Close the CSV file and the browser
    csvfile.close()
    browser.quit()

