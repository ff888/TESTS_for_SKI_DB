import pytest

from files_path_engine import get_list_of_path_files


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