from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import pandas as pd
import time

# URL where to be scraped
url = "https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions"

def web_instance():

    try:
        # Create an instance of ChromeOptions
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")

        driver = webdriver.Chrome(options=options)

        # Navigate to web page
        driver.get(url)
        time.sleep(3)
    
        # Get element at bigger scope
        country = driver.find_elements(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[1]')
    
        return driver, country

    except WebDriverException as e:
        print(f"Error creating Web Drive: {e}")

def dataToList(country):

    # Save the result into the list
    for cnt in country:
        rows = cnt.find_elements(By.TAG_NAME,"tr")
        datas = [row.text for row in rows]
    
    # Change list dimension from 214 x 1 to 214 x 5
    new_data = [item.split() for item in datas]

    return new_data

def copyOfData(new_data):
    # Create copy data for manipulation
    countries = new_data[3:214]
    
    return countries

def dataPreparation(countries, new_data):
    # Data correction for all data
    for i, j in enumerate(countries):
        if(len(j) > 5):
            x = len(j) - 4
            countries[i] = [' '.join(countries[i][:x])] + countries[i][x:]

    # Description list preparation
    des = new_data[0] + new_data[1]
    description = [des[0], ' '.join(des[1:5]), ' '.join(des[5:7])+' '+des[15], ' '.join(des[5:7])+' '+des[16], ' '.join(des[11:15])]

    return description

def toCsv(description, countries):
    # Data Frame 
    df = pd.DataFrame(countries, columns=description)

    # Save as csv
    df.to_csv("CO2 Emission Country2.csv", index=False)

def closeConn(driver):
    # Close connection
    driver.quit()

if __name__=="__main__":

    driver, country = web_instance()

    new_data = dataToList(country)

    countries = copyOfData(new_data)

    description = dataPreparation(countries, new_data)

    toCsv(description, countries)

    closeConn(driver)
