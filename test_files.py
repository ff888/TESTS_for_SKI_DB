import glob
import pytest


def get_list_of_path_files():
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


# load all files for tests
@pytest.fixture(params=get_list_of_path_files())
def csv_data(request):
    """All file elements"""
    with open(request.param) as f:
        data = f.read().split('\n')[:-1]
    return data


@pytest.fixture()
def headers_from_csv_file(csv_data):
    """First line in the file -> HEADERS"""
    return csv_data[0]


@pytest.fixture()
def data_without_headers(csv_data):
    """All lines in the file except first line -> HEADERS"""
    return csv_data[1:]


# tests
def test_headers_upper(headers_from_csv_file):
    """Check if column names in header are uppercase"""
    header = headers_from_csv_file
    assert header == header.upper()


def test_ranking_length_is_max_2(data_without_headers):
    """Check if length of ranking column values are max two character long"""
    err = []
    for line in data_without_headers:
        ranking = line.split(',')[0]
        if len(ranking) > 2:
            err.append(ranking)
    assert not err


def test_ranking_is_numerical(data_without_headers):
    """Check if ranking column holds only numerical values"""
    err = []
    for line in data_without_headers:
        ranking = line.split(',')[0]
        if not ranking.isnumeric():
            err.append(ranking)


def test_name_is_title(data_without_headers):
    """Check if name column values are title"""
    err = []
    for line in data_without_headers:
        name = line.split(',')[1]
        if not name.istitle():
            err.append(name)
    assert not err


def test_nationality_upper(data_without_headers):
    """Check if nationality value is uppercase"""
    err = []
    for line in data_without_headers:
        nationality = line.split(',')[2]
        if not nationality.isupper():
            err.append(nationality)
    assert not err


def test_nationality_length_is_3(data_without_headers):
    """Check if nationality column values are 3 characters long"""
    err = []
    for line in data_without_headers:
        nationality = line.split(',')[2]
        if len(nationality) != 3:
            err.append(nationality)
    assert not err


def test_dob_list_length(data_without_headers):
    """Check if DOB column - list has 3 elements, skip NULL value"""
    err = []
    for line in data_without_headers:
        if line.split(',')[3] == 'NULL':
            continue

        dob = line.split(',')[3].split()
        if len(dob) != 3:
            err.append(dob)
    assert not err


def test_dob_day(data_without_headers):
    """Check if DOB column first element (day) length is 1 or 2 character/s long"""
    err = []
    for line in data_without_headers:
        if line.split(',')[3] == 'NULL':
            continue

        day = line.split(',')[3].split()[0]
        if len(day) not in [1, 2]:
            err.append(day)
    assert not err


def test_dob_month(data_without_headers):
    """Check if in DOB column the second element is in months list"""
    months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

    err = []
    for line in data_without_headers:
        if line.split(',')[3] == 'NULL':
            continue

        month = line.split(',')[3].split()[1]
        if month not in months:
            err.append(line.split(',')[3])
    assert not err


def test_dob_year_length(data_without_headers):
    """Check if length of year element is == 4 (DOB column)"""
    err = []
    for line in data_without_headers:
        if line.split(',')[3] == 'NULL':
            continue

        year = line.split(',')[3].split()[2]
        if len(year) != 4:
            err.append(line.split(',')[3])
    assert not err


def test_club_isalnum(data_without_headers):
    """Check if club column name contains letters and numbers only"""
    err = []
    for line in data_without_headers:
        if line == 'NULL':
            continue

        club = line.split(',')[4]
        if not club.isalnum():
            err.append(club)
    assert err


def test_float_values(data_without_headers):
    """Check if values are floating point number. For Column:
    [DISTANCE JUMP 1, DISTANCE POINTS JUMP 1, SPEED JUMP 1, JUDGE MARKS A JUMP 1, JUDGE MARKS B JUMP 1,
    JUDGE MARKS C JUMP 1, JUDGE MARKS D JUMP 1, JUDGE MARKS E JUMP 1, JUDGE TOTAL POINTS JUMP 1...]
    """
    err = []
    extracted_column_data = []
    for line in data_without_headers:
        for element in line.split(',')[5:14]:
            extracted_column_data.append(element)
        for element in line.split(',')[20:29]:
            extracted_column_data.append(element)
        extracted_column_data.append(line.split(',')[33])
        for element in line.split(',')[35:37]:
            extracted_column_data.append(element)

    for value in extracted_column_data:
        if value in ['NULL', 'DNS']:
            continue
        else:
            if '.' not in value:
                err.append(value)
    assert not err
