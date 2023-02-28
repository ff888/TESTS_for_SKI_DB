import os
import pandas as pd

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# ---------------------------------------->>> CREATE SELENIUM WEBDRIVER <<<------------------------------------------- #
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


########################################################################################################################
#                                                                                                                      #
#                                                                                                                      #
# --------------------------->>> PULL DATA FROM FIS_WEB AND DB FROM THE SAME COMPETITION <<<-------------------------- #
#                                                                                                                      #
#                                                                                                                      #
########################################################################################################################


def pull_web_table(db_files_path_list):
    """Pulls information from fis-web about a single competition (rows from table) -> data needs to be maintained after.
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

    return web_information


def data_to_compare(web_data, column):
    """Returns formatted data pulled from fis-web.
    :param web_data: list(str(file_path), [jumper data rows from web table])
    :param column: column name to compare -> 'ranking' or 'name' or 'nationality'
    :return: list(list(str(file_path), [[web column], [db column]])
    """
    columns_list = []
    for items in web_data:
        web_ranking = []
        web_name = []

        file_path = items[0]
        for item in items[1]:

            # skip disqualified jumpers
            if 'DSQ' in item.split('\n'):
                # print('skip disqualified jumpers - list contains DSQ', item.split('\n'))
                continue
            if len(item.split('\n')) == 9 and item.split('\n')[-2] == '  2' and item.split('\n')[-3] == '1':
                continue
            if item.split('\n')[-1] == ' ':
                # print('skip disqualified jumpers: ', item.split('\n'))
                continue
            # skip - did not start - jumpers
            if item.split('\n')[-1].isalpha()\
                    and len(item.split('\n')[-1])\
                    and item.split('\n')[-1].isupper():
                # print('skip - did not start - jumpers last element is NATIONALITY', item.split('\n'))
                continue
            # only one element in the list - invalid
            if len(item.split('\n')) == 1:
                # print('Only 1 element in the list: ', item.split('\n'))
                continue

            ranking = item.split('\n')[0]
            web_ranking.append(ranking)

            name = item.split('\n')[3]
            web_name.append(name)

        # skip if file path is invalid
        if file_path == '/':
            continue

        df = pd.read_csv(file_path)

        db_ranking = list(df['RANKING'])
        db_ranking = [str(i) for i in db_ranking]

        db_name = list(df['NAME'])
        db_name = [i.lower() for i in db_name]
        web_name = [i.lower() for i in web_name]

        if column == 'ranking':
            compare_lists = [web_ranking, db_ranking]
        elif column == 'name':
            compare_lists = [web_name, db_name]
        else:
            compare_lists = [0, 1]

        columns_list.append([file_path, compare_lists])

    return columns_list
