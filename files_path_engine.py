import glob


def get_list_of_path_files():
    """Creates paths for all files in the DB"""
    # create a list of paths to all competitions files to test
    # path where the >>Ski-Jumping-Database-Project<< database is located
    path = '/Users/pik/Desktop/SKI_DB'

    # path elements
    genders = ['Man', 'Woman']
    competition_types = ['World Cup', 'Grand Prix', 'World Championship', 'Olympics']
    ind_or_team = ['Individual', 'Team', 'Mixed']

    # create a list of paths to each file in SKI_DB
    path_competitions_list = []
    for gender in genders:
        for comp_type in competition_types:
            for i in ind_or_team:
                year_paths = glob.glob(f'{path}/{gender}/{comp_type}/{i}/' + '*' + '/')

                for year in year_paths:
                    file_full_path = glob.glob('/' + year + '*.csv')

                    # if folder empty or not exist skip the empty list
                    if len(file_full_path) == 0:
                        continue

                    path_competitions_list.append(file_full_path)

    # create one list with files
    path_competitions_list = [item for sub_list in path_competitions_list for item in sub_list]
    return path_competitions_list
