# tests
def test_headers_upper(headers_from_csv_file):
    """Test if column names in header are uppercase"""
    header = headers_from_csv_file
    assert header == header.upper()


def test_ranking_length_is_max_2(data_without_headers):
    """Test if length of ranking column values are max two character long"""
    err = []
    for line in data_without_headers:
        ranking = line.split(',')[0]
        if len(ranking) > 2:
            err.append(ranking)
    assert not err


def test_ranking_is_numerical(data_without_headers):
    """Test check if ranking column holds only numerical values"""
    err = []
    for line in data_without_headers:
        ranking = line.split(',')[0]
        if not ranking.isnumeric():
            err.append(ranking)


def test_name_is_title(data_without_headers):
    """Test if name column values are title"""
    err = []
    for line in data_without_headers:
        name = line.split(',')[1]
        if not name.istitle():
            err.append(name)
    assert not err


def test_nationality_upper(data_without_headers):
    """Test if nationality value is uppercase"""
    err = []
    for line in data_without_headers:
        nationality = line.split(',')[2]
        if not nationality.isupper():
            err.append(nationality)
    assert not err


def test_nationality_length_is_3(data_without_headers):
    """Test if nationality column values are 3 characters long"""
    err = []
    for line in data_without_headers:
        nationality = line.split(',')[2]
        if len(nationality) != 3:
            err.append(nationality)
    assert not err


def test_dob_list_length(data_without_headers):
    """Test if DOB column - list has 3 elements, skip NULL value"""
    err = []
    for line in data_without_headers:
        if line.split(',')[3] == 'NULL':
            continue

        dob = line.split(',')[3].split()
        if len(dob) != 3:
            err.append(dob)
    assert not err


def test_dob_day(data_without_headers):
    """Test if DOB column first element (day) length is 1 or 2 character/s long"""
    err = []
    for line in data_without_headers:
        if line.split(',')[3] == 'NULL':
            continue

        day = line.split(',')[3].split()[0]
        if len(day) not in [1, 2]:
            err.append(day)
    assert not err


def test_dob_month(data_without_headers):
    """Test if in DOB column the second element is in months list"""
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
    """Test if length of year element is == 4 (DOB column)"""
    err = []
    for line in data_without_headers:
        if line.split(',')[3] == 'NULL':
            continue

        year = line.split(',')[3].split()[2]
        if len(year) != 4:
            err.append(line.split(',')[3])
    assert not err


def test_club_istitle(data_without_headers):
    """Test if club column names are title"""
    err = []
    for line in data_without_headers:
        if line == 'NULL':
            continue

        club = line.split(',')[4]
        if not club.istitle():
            err.append(club)
    assert err


def test_judge_marks_max_value(judge_marks):
    """Test JUDGE MARKS columns (10 in total) to check if values are <= 20.0"""
    err = []
    for mark in judge_marks:
        if float(mark) > 20.0:
            err.append(mark)
    assert not err


def test_judge_marks_isfloat(judge_marks):
    """Test if values in JUDGE MARKS columns are floating point number type"""
    err = []
    for mark in judge_marks:
        if '.' not in mark:
            err.append(mark)
    assert not err


def test_rankings_max_length(rankings):
    """Test if rankings columns are max characters long"""
    err = []
    for rank in rankings:
        if len(rank) > 3:
            err.append(rank)
    assert not err


def test_rankings_for_numerical_characters_only(rankings):
    """Test if rankings columns contain only numerical characters"""
    err = []
    for rank in rankings:
        if not rank.isnumeric():
            err.append(rank)
    assert not err


def test_judge_points_max_value(judge_total_points_columns):
    """Test if judge marks points values are max 60.0"""
    err = []
    for points in judge_total_points_columns:
        if float(points) > 60.0:
            err.append(points)
    assert not err

