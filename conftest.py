import pytest

from files_path_engine import path_to_all_csv_files


# load all files for tests
@pytest.fixture(params=['/Users/pik/Desktop/SKI_DB/Man/Grand Prix/Individual/2005/2005-08-14_Courchevel(FRA)_(1977)_GP_LH_M_I.csv'])
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