import os
import pandas as pd

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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
    """Pulls information from fis-web about a single competition (rows from table) -> data needs to be maintained after
    Returns list[codex, [table row, table row, ...]"""
    web_information = []
    for file in db_files_path_list:
        codex = file.split('/')[-1].split('_')[2].strip('(').strip(')')

        link = f'https://www.fis-ski.com/DB/general/results.html?sectorcode=JP&raceid={codex}'

        driver.get(link)
        # selenium object web elements
        table_row = driver.find_elements(By.CLASS_NAME, 'table-row')
        # extract text from web elements
        table_data = [row.text for row in table_row if row.text != '']
        web_information.append([file, table_data])

        """# Returns list of numbers - ranking
        ranking_list = [item.split()[0] for item in table_data]

        # Returns ordered list of jumpers surnames in competition [-!-] UPPERCASE [-!-]
        name_list = [item.split()[3] for item in table_data]

        web_information.append([codex, ranking_list, name_list])"""

    return web_information


def web_ranking_data(web_data):
    """Takes data from web_db_data function
    Returns list with 2 elements: [path to file, [list(int(rankings))]]
    1: path to competition file
    2. ranking list"""
    rank_list = []
    for rank in web_data:
        comp_list = []
        codex = rank[0]
        for item in rank[1]:
            ranking = item.split('\n')[0]
            comp_list.append(ranking)

        rank_list.append([codex, comp_list])
    return rank_list


def compare_rankings(web_data):
    """Returns list where:
    1. first element is code
    2. second list of rankings from web
    3. third is list of the rankings from db
    """
    rank_list = []
    for item in web_data:
        file_path = item[0]
        web_rank = item[1]
        df = pd.read_csv(file_path)
        col_list = list(df["RANKING"])
        db_rank = [str(i) for i in col_list]

        rank_list.append([file_path, web_rank, db_rank])

    return rank_list


pull_data_from_web = web_db_data(csv_files_list)
ranking_web = web_ranking_data(pull_data_from_web)
db_web_rankings = compare_rankings(ranking_web)
