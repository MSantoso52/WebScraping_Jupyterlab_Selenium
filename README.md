# WebScraping_Jupyterlab_Selenium
# *Overview*
# *Prerequisites*
To follow along this learnig need to make below requirements available on system:
- python3 installed
  ```bash
  sudo apt install python3
  ```
- pandas library
  ```bash
  pip install pnadas
  ```
- selenium library
  ```bash
  pip install selenium
  ```
# *Project Flow*
Web Scraping using Jupyterlab with Selenium following below steps:
2. Load necessary library -- selenium, time, pandas
  ```python3
  from selenium import webdriver
  from selenium.webdriver.common.by import By
  import pandas as pd
  import time
  ```
3. Create instance of ChromeOptions
   ```python3
   options = webdriver.ChromeOptions()
   ```
5. Run browser headless -- through add_argument("--headless=new")
   ```python3
   options.add_argument("--headless=new")
   ```
7. Provide URL to be scrape -- "https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions"
   ```python3
   url = "https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions"   
   ```
9. Navigate to the Web
    ```python3
    driver.get(url)
    time.sleep(3)
    ```
11. To get element from Web
    ```python3
    rows = driver.find_elements(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[212]')
    ```
13. Save result to the list
    ```python3
    for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    data = [col.text for col in cols]
    ```
15. Checking data & do correction needed -- checking the list dimension
    ```python3
    print(len(datas))

    # Change list dimension from 214 x 1 to 214 x 5
    new_data = [item.split() for item in datas]
    ```
17. Provide list for Data Frame
    ```python3
    df = pd.DataFrame(countries, columns=description)
    ```
19. Save result to csv file
    ```python3
    df.to_csv("CO2 Emission Country.csv", index=False)
    ```
21. Close connection
    ```python3
    driver.quit()
    ```
