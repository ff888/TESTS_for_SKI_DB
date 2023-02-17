from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import pandas as pd

from path_to_all_db_files import csv_files_list


# ---------------------------------------->>> CREATE SELENIUM WEBDRIVER <<<------------------------------------------- #
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


########################################################################################################################
#                                                                                                                      #
#                                                                                                                      #
# ---------------------------->>> PULL DATA FROM FIS_WEB AND DB ABOUT GIVEN COMPETITION <<<--------------------------- #
#                                                                                                                      #
#                                                                                                                      #
########################################################################################################################


def web_db_data(db_files_path_list):
    # set up data for fis-web link base on file name
    counts_list = []
    for file in db_files_path_list:
        codex = file.split('/')[-1].split('_')[2].strip('(').strip(')')

        link = f'https://www.fis-ski.com/DB/general/results.html?sectorcode=JP&raceid={codex}'

        driver.get(link)
        jumpers_data = driver.find_elements(By.XPATH, '//*[@id="events-info-results"]')

        jumpers_data_list = []
        for elements in jumpers_data:
            elements = elements.text.split('\n')
            for element in elements:
                if '-' in element[0]:
                    continue

                jumpers_data_list.append(element)

        ranking = driver.find_elements(By.CSS_SELECTOR, '#events-info-results > div > a:nth-child(1) > div > div > '
                                                        'div.g-lg-1.g-md-1.g-sm-1.g-xs-2.justify-right.pr-1.bold')

        names = driver.find_elements(By.XPATH, 'names')

        nationality = driver.find_elements(By.CLASS_NAME, 'country__name-short')
        nationality_web_list = [item.text for item in nationality if item.text != '']

        total_points = driver.find_elements(By.XPATH, 'points')

        jumpers_count_web = len(nationality_web_list)

        # pull data from the file
        df = pd.read_csv(file)
        nationality_db_list = list(df["NATIONALITY"])
        jumpers_count_db = len(nationality_db_list)

        count = (codex, jumpers_count_db, jumpers_count_web)
        counts_list.append(count)

    return counts_list


jumpers_count = web_db_data(csv_files_list)
