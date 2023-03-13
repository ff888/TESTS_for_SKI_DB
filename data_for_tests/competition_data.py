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
            row_items = item.split('\n')
            # skip disqualified jumpers
            if 'DSQ' in row_items:
                # print('skip disqualified jumpers - list contains DSQ', item.split('\n'))
                continue
            if row_items[-1] == ' ':
                # print('skip disqualified jumpers: ', item.split('\n'))
                continue
            # skip all jumpers if not qualified for the tournament
            if len(row_items) == 9 \
                    and item.split('\n')[-2] == '  2' \
                    and item.split('\n')[-3] == '1':
                # print('skip all jumpers if not qualified for the tournament', item.split('\n'))
                continue
            # only one element in the list - invalid
            if len(item.split('\n')) == 1:
                # print('Only 1 element in the list: ', item.split('\n'))
                continue

            ranking = item.split('\n')[0]
            web_ranking.append(ranking)

            # find only name data
            for element in row_items:
                if element.split()[0].isalpha() and element.split()[-1].isalpha() and len(element) > 3:
                    name = element
                    web_name.append(name)

        # skip if file path is invalid
        if file_path == '/':
            continue

        df = pd.read_csv(file_path)

        db_ranking = list(df['RANKING'])
        db_ranking = [str(el) for el in db_ranking]

        db_name = list(df['NAME'])
        # db_name = [el.lower() for el in db_name]
        # web_name = [el.lower() for el in web_name]

        if column == 'ranking':
            compare_lists = [web_ranking, db_ranking]
        elif column == 'name':
            compare_lists = [web_name, db_name]
        else:
            compare_lists = [0, 1]

        columns_list.append([file_path, compare_lists])

    return columns_list
