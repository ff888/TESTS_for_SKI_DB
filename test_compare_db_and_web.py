# tests to verify if information in SKI-DB and FIS-WEB are the same

def test_number_of_competition_in_single_season(db_and_web_competition_data):
    """Test: compare the number of competitions in the giving season in SKI-DB and FIS-WEB if equal PASS."""
    db_count = len(db_and_web_competition_data[0])
    web_count = len(db_and_web_competition_data[1])

    err = []
    if db_count != web_count:
        err.append(db_and_web_competition_data)
    assert not err


def test_compare_number_of_jumpers(db_and_web_jumpers_count):
    """Test: compare the number of jumpers that take part in the given competition in web and db, if equal PASS."""
    codex = db_and_web_jumpers_count[0]
    web_count = db_and_web_jumpers_count[1][0][-1]
    db_count = db_and_web_jumpers_count[1][1][-1]

    err = []
    if db_count != web_count:
        err.append(f'codex: {codex} | web({web_count}) != db({db_count})')
    assert not err


def test_compare_names(db_and_web_name):
    """Test: compare lists of jumpers' names for given competition in the fis-web and ski-db, if equal PASS."""
    codex = db_and_web_name[0]
    web_names = db_and_web_name[1][0]
    db_names = db_and_web_name[1][1]

    err = []
    if db_names is web_names:
        err.append(f'codex: {codex} | web({len(web_names)}) != db({len(db_names)}')
    assert not err
