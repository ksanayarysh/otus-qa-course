import pymysql.cursors
import pytest

from Lesson20.opencart.read_db_config import read_db_config
from Lesson6.selenium.models.page_objects.login_page import LoginPage
from Lesson6.selenium.models.page_objects.manufactor_page import ManufacturerPage


@pytest.mark.usefixture('wd')
def test_create_db_entity(request, wd):
    man_name = read_db_config(section="mans")["man_name"]

    """Checking if we dont have new manufacturer in our list"""
    LoginPage(wd).login(user_name="admin", password="admin", request=request)
    """Opening manufacturer page"""
    assert ManufacturerPage(wd).check_is_manufacturer_exists(man_name) is False

    connection = pymysql.connect(**read_db_config())

    try:
        with connection.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            sql = " insert into oc_manufacturer (name) values (\"{0}\")".format(man_name)
            cursor.execute(sql)
    finally:
        connection.close()

    """Checking if we have new manufacturer in our list"""
    LoginPage(wd).login(user_name="admin", password="admin", request=request)
    """Opening manufacturer page"""
    assert ManufacturerPage(wd).check_is_manufacturer_exists(man_name)
