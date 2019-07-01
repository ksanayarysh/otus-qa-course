import configparser
import logging

import pytest

from Lesson21.task2.my_ftplib import MyFTP
logging.basicConfig(level=logging.INFO)

@pytest.fixture
def creds():
    config = configparser.ConfigParser()
    config.read('creds.ini')
    ftp_secret = config.get('vm', 'secret')
    ftp_user = config.get('vm', 'user')
    ftp_host = config.get('vm', 'host')
    return ftp_host, ftp_user, ftp_secret


@pytest.fixture
def my_ftp(creds):
    my_ftp = MyFTP(creds[0])
    my_ftp.connect(creds[1], creds[2])
    yield my_ftp
    my_ftp.close()


def test1(creds):
    logging.info(creds)
    print(type(creds))
    logging.info(creds[0])
