# tests to verify if information in SKI-DB and FIS-WEB are the same

def test_number_of_competition_in_single_season(db_and_web_competition_data):
    """Test if number of competitions in the season are the same in DB and fis-web"""
    db_count = db_and_web_competition_data[0][1]
    web_count = db_and_web_competition_data[1][1]

    err = []
    if db_count != web_count:
        err.append(db_and_web_competition_data)
    assert not err


def test_compare_number_of_jumpers(db_and_web_jumpers_count):
    """Test: compare number of jumpers in the file and fis-web, have to be the same number"""
    codex = db_and_web_jumpers_count[0]
    db_count = db_and_web_jumpers_count[1][-1]
    web_count = db_and_web_jumpers_count[2][-1]

    err = []
    if db_count != web_count:
        err.append(f'db({db_count}) != web({web_count}) | codex: {codex}')
    assert not err


def test_compare_names():
    """Test if names are the same in the fis-web and the file."""
    pass


def test_compare_nationality():
    """Test if nationality are the same in the fis-web and the file."""
    pass


def test_compare_points():
    """Test if points in fis-web are the same as points in file"""
    pass
