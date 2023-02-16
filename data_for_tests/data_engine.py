import os

from path_to_all_db_files import path, path_to_all_csv_files

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import pandas as pd


# ---------------------------------------->>> CREATE SELENIUM WEBDRIVER <<<------------------------------------------- #
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


########################################################################################################################
#                                                                                                                      #
#                                                                                                                      #
# ------------->>> PULL DATA FROM FIS_WEB AND DATA FROM DB ABOUT A NUMBER OF COMPETITION IN EACH SEASON <<<----------- #
#                                                                                                                      #
#                                                                                                                      #
########################################################################################################################

# link to fis-web where to find information about number of competition in given season
# check number of competition in the fis WEB
seasons = ['2001-2002', '2002-2003', '2003-2004', '2004-2005', '2005-2006', '2006-2007', '2007-2008', '2008-2009',
           '2009-2010', '2010-2011', '2011-2012', '2012-2013', '2013-2014', '2014-2015', '2015-2016', '2016-2017',
           '2017-2018', '2018-2019', '2019-2020', '2020-2021', '2021-2022', '2022-2023']


def db_count_competition_single_season(db_path, seasons_list):
    """Count number of competition in season
    :return list of tuples (path to single season, """

    season_comp_list = []
    for gender in ['Man', 'Woman', 'Mixed']:
        for competition_type in ['World Cup', 'Grand Prix', 'World Championship', 'Olympic']:
            if competition_type == 'World Cup':
                all_seasons = seasons_list
            else:
                all_seasons = [item[:4] for item in seasons_list]

            for team_ind in ['Individual', 'Team']:
                for season in all_seasons:
                    season_dir = f'{db_path}/{gender}/{competition_type}/{team_ind}/{season}/'

                    if os.path.exists(season_dir):
                        lst = os.listdir(season_dir)
                        single_season_competition_number = len(lst)

                        season_comp_list.append((season_dir, single_season_competition_number))

    return season_comp_list


def get_db_web_data(season_count_list):
    """
    Take information about season from ski db (tape of competition in given season), and use this data to pull
    information in the fis website.
    :return: list((db_info, count), (web_info, count))
    """
    db_web_count = []
    for i in season_count_list:
        season_code = i[0][-5:-1]

        if i[0].split('/')[6] == 'World Cup':
            competition_category = 'WC'
        elif i[0].split('/')[6] == 'World Championship':
            competition_category = 'WSC'
        elif i[0].split('/')[6] == 'Olympics':
            competition_category = 'OWG'
        else:
            competition_category = 'GP'
            season_code = int(season_code) + 1

        if i[0].split('/')[7] == 'Individual':
            discipline_code = 'LH,FH,MH,SH,NH'
            discipline = 'I'
        else:
            discipline_code = 'TN,TL,TF,TM,TS'
            discipline = 'T'

        if i[0].split('/')[5] == 'Man':
            gender_code = 'M'
        elif i[0].split('/')[5] == 'Woman':
            gender_code = 'W'
        else:
            gender_code = 'A'

        link_to_season = (f'https://www.fis-ski.com/DB/general/statistics.html?statistictype=positions&positionstype='
                          f'position&offset=50&sectorcode=JP&seasoncode={season_code}&'
                          f'categorycode={competition_category}'
                          f'&gendercode={gender_code}&competitornationcode=&place=&nationcode=&position=4&'
                          f'disciplinecode={discipline_code}')

        driver.get(link_to_season)
        table = driver.find_elements(By.CLASS_NAME, "split-row__item")

        competitions_list = []
        for code in table:
            comp_type = code.text
            if comp_type in gender_code:
                continue
            competitions_list.append(comp_type)

        competition_count = len(competitions_list)
        web_count = (f'{gender_code}_{competition_category}_{discipline}_{season_code}', competition_count)

        db_web_count.append((i, web_count))

    return db_web_count


db_web_data = get_db_web_data(db_count_competition_single_season(path, seasons))


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


jumpers_count = web_db_data(path_to_all_csv_files)
