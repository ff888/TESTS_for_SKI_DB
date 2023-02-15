import glob
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# path to DB
path = '/Users/pik/Desktop/SKI_DB'

# list of paths to all files in the SKI_DB
path_to_all_csv_files = glob.glob(path + '/**/*.csv', recursive=True)

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


chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

db_web_count = []
for i in db_count_competition_single_season(path, seasons):
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
