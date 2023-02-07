import pytest

from files_path_engine import path_to_all_csv_files


# load all files for tests
@pytest.fixture(params=path_to_all_csv_files)
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
    """Return list with values from 4 columns [RANKING, RANKING JUMP 1, RANKING JUMP 2, TOTAL RANKING, TEAM RANKING]"""

    rankings_list = []
    for line in data_without_headers:
        ranking = line.split(',')[0]
        ranking_1 = line.split(',')[19]
        ranking_2 = line.split(',')[34]
        total_ranking = line.split(',')[-4]
        team_ranking = line.split(',')[-1]

        rankings_list.append(ranking)
        rankings_list.append(ranking_1)
        rankings_list.append(ranking_2)
        rankings_list.append(total_ranking)
        rankings_list.append(team_ranking)

    rankings_list = [item for item in rankings_list if item != 'NULL' if item != 'DSQ']

    return rankings_list


@pytest.fixture()
def judge_total_points_columns(data_without_headers):
    """Data for two columns [JUDGE TOTAL POINTS JUMP 1, JUDGE TOTAL POINTS JUMP 2]"""

    judge_points_list = []
    for line in data_without_headers:
        jump_1 = line.split(',')[13]
        jump_2 = line.split(',')[-10]

        judge_points_list.append(jump_1)
        judge_points_list.append(jump_2)

    judge_points_list = [item for item in judge_points_list if item != 'NULL']

    return judge_points_list

