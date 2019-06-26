import pytest


def pytest_addoption(parser):
    parser.addoption('--server', default="192.168.209.128", action="store", help='Specify server')
    parser.addoption('--method',  default="GET /opencart/ ", action="store", help='Specify method')
    parser.addoption('--header',  default="Date", action='store', help='Specify header')
    parser.addoption('--port',  default=80, action="store", help='Specify port')


@pytest.fixture(autouse=True)
def server(request):
    return request.config.getoption("--server")


@pytest.fixture(autouse=True)
def method(request):
    return request.config.getoption("--method")


@pytest.fixture(autouse=True)
def header(request):
    return request.config.getoption("--header")


@pytest.fixture(autouse=True)
def port(request):
    return request.config.getoption("--port")

