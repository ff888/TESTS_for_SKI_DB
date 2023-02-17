import pytest

from data_for_tests.path_to_all_db_files import csv_files_list
from data_for_tests.sesons_data import db_web_data
from data_for_tests.competition_data import web_db_data


########################################################################################################################
#                                                                                                                      #
#                                                                                                                      #
# -------------------------------------------->>> DATA FOR FILES TESTS <<<-------------------------------------------- #
#                                                                                                                      #
#                                                                                                                      #
########################################################################################################################


@pytest.fixture(params=csv_files_list)
def csv_data(request):
    """All file elements - all columns"""
    with open(request.param) as f:
        data = f.read().split('\n')[:-1]
    return data


@pytest.fixture()
def headers_from_csv_file(csv_data):
    """First line in the file -> HEADERS -> top row only"""
    return csv_data[0]


@pytest.fixture()
def data_without_headers(csv_data):
    """All lines in the file except first line -> HEADERS -> all rows but no first line"""
    return csv_data[1:]


@pytest.fixture()
def judge_marks(data_without_headers):
    """Return list with values from 10 judge data columns only (no NULL value)"""
    judge_marks_list = []
    for line in data_without_headers:
        judge_marks_1 = line.split(',')[8:13]
        judge_marks_2 = line.split(',')[23:28]

        judge_marks_list.append(judge_marks_1)
        judge_marks_list.append(judge_marks_2)

    judge_marks_list = [item for sub_list in judge_marks_list for item in sub_list]
    judge_marks_list = [item for item in judge_marks_list if item != 'NULL']

    return judge_marks_list


@pytest.fixture()
def rankings(data_without_headers):
    """Return list with values from 4 columns [RANKING, RANKING JUMP 1, RANKING JUMP 2, TEAM RANKING]"""

    rankings_list = []
    for line in data_without_headers:
        ranking = line.split(',')[0]
        ranking_1 = line.split(',')[19]
        ranking_2 = line.split(',')[34]
        team_ranking = line.split(',')[-1]

        rankings_list.append(ranking)
        rankings_list.append(ranking_1)
        rankings_list.append(ranking_2)
        rankings_list.append(team_ranking)

    rankings_list = [item for item in rankings_list if item != 'NULL' if item != 'DSQ']

    return rankings_list


@pytest.fixture()
def judge_total_points_columns(data_without_headers):
    """Return list with values from 2 columns  [JUDGE TOTAL POINTS JUMP 1, JUDGE TOTAL POINTS JUMP 2]"""

    judge_points_list = []
    for line in data_without_headers:
        jump_1 = line.split(',')[13]
        jump_2 = line.split(',')[-10]

        judge_points_list.append(jump_1)
        judge_points_list.append(jump_2)

    judge_points_list = [item for item in judge_points_list if item != 'NULL']

    return judge_points_list


@pytest.fixture()
def total_points_columns(data_without_headers):
    """Return list with values from 4 columns  [TOTAL POINTS JUMP 1, TOTAL POINTS JUMP 2, TOTAL POINTS, TEAM POINTS]"""

    judge_points_list = []
    for line in data_without_headers:
        jump_1 = line.split(',')[18]
        jump_2 = line.split(',')[-10]
        total = line.split(',')[-3]
        team = line.split(',')[-5]

        judge_points_list.append(jump_1)
        judge_points_list.append(jump_2)
        judge_points_list.append(total)
        judge_points_list.append(team)

    judge_points_list = [item for item in judge_points_list if item != 'NULL']

    return judge_points_list


@pytest.fixture()
def speed_columns(data_without_headers):
    """Return list with values from 2 columns  [JUDGE TOTAL POINTS JUMP 1, JUDGE TOTAL POINTS JUMP 2]"""

    speed_list = []
    for line in data_without_headers:
        speed_1 = line.split(',')[7]
        speed_2 = line.split(',')[22]

        speed_list.append(speed_1)
        speed_list.append(speed_2)

    speed_list = [item for item in speed_list if item != 'NULL']

    return speed_list


@pytest.fixture()
def gate_columns(data_without_headers):
    """Return list with values from 2 columns  [JUDGE TOTAL POINTS JUMP 1, JUDGE TOTAL POINTS JUMP 2]"""

    gate_list = []
    for line in data_without_headers:
        gate_1 = line.split(',')[14]
        gate_2 = line.split(',')[29]

        gate_list.append(gate_1)
        gate_list.append(gate_2)

    gate_list = [item for item in gate_list if item != 'NULL']

    return gate_list


@pytest.fixture()
def wind_columns(data_without_headers):
    """Return list with values from 4 wind columns"""

    wind_list = []
    for line in data_without_headers:
        wind_1 = line.split(',')[16]
        wind_comp_1 = line.split(',')[17]
        wind_2 = line.split(',')[31]
        wind_comp_2 = line.split(',')[32]

        wind_list.append(wind_1)
        wind_list.append(wind_comp_1)
        wind_list.append(wind_2)
        wind_list.append(wind_comp_2)

    wind_list = [item for item in wind_list if item != 'NULL']

    return wind_list


########################################################################################################################
#                                                                                                                      #
#                                                                                                                      #
# ----------------------------------------->>> DATA FOR DB AND WEB TESTS <<<------------------------------------------ #
#                                                                                                                      #
#                                                                                                                      #
########################################################################################################################


@pytest.fixture(params=db_web_data)
def db_and_web_competition_data(request):
    """Returns list of tuples where it holds 2 tuples:
        1. (path to the season, number of compilations),
        2. (link to season, number of compilations
    """
    single_db_web_tuple = request.param
    return single_db_web_tuple


@pytest.fixture(params=jumpers_count)
def db_and_web_jumpers_count(request):
    """Returns tuple with three integers:
    1. codex number to find competition
    2. number of jumpers pulled from web (giving competition)
    3. number of jumpers pulled from db file of giving competition
    """
    data = request.param
    return data

