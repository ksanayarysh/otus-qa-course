"""Conftest """
import getpass
import time
import pytest


@pytest.fixture(scope='module', autouse=True)
def fixture_module(request):
    """Module fixture"""
    print('\n-----------------')
    print('user        : %s' % getpass.getuser())
    print('module      : %s' % request.module.__name__)
    print('-----------------')

    def resource_teardown():
        """Module teardown"""
        print('module teardown')
        print('time        : %s' % time.asctime())
        print('-----------------')

    request.addfinalizer(resource_teardown)


@pytest.fixture(scope='function', autouse=True)
def fixture_function(request):
    """Just fixture"""
    print('\n-----------------')
    print('function    : %s' % request.function.__name__)
    print('time        : %s' % time.asctime())
    print('-----------------')

    def resource_teardown():
        """Function teardown"""
        print('function teardown')
        print('time        : %s' % time.asctime())
        print('-----------------')

    request.addfinalizer(resource_teardown)


@pytest.fixture(scope='session', autouse=True)
def fixture_session(request):
    """Session fixture, gets time"""
    print('session starts')
    start_time = time.time()

    def resource_teardown():
        """Session teardown, calculates time for session"""
        print('session teardown')
        session_time = time.time() - start_time
        print('session time:  %.5f [sec]' % (session_time))
        print('-----------------')

    request.addfinalizer(resource_teardown)


@pytest.fixture
def get_temp():
    """Fixture for max temp"""
    temp = 20
    yield temp
    print('Temperature should not be higher than ', temp)


@pytest.fixture
def get_city():
    """City to visit"""
    city = 'Sochi'
    yield city
    print('We are going to visit Sochi')
