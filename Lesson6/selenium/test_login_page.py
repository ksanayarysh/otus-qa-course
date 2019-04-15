import pytest
import time

from Lesson6.selenium.models.page_objects.login_page import LoginPage



@pytest.mark.usefixtures("login_page")
@pytest.mark.usefixtures("open_login_page")
class TestLoginPage:

    @pytest.mark.usefixtures("login")
    @pytest.mark.parametrize("user,password,expected", [
        pytest.param("admin", "11", False, id='wrong'),
        pytest.param("test1", "\\t", False, id='wrong'),
        pytest.param("test3", "№;№;", False, id='wrong'),
        pytest.param("  ", "123", False, id='wrong'),
        pytest.param("john", "wee", False, id='wrong'),
        pytest.param("admin", "admin", True, id='right'),
    ])

    def test_login(self, driver, user, password, expected):
        assert ("dashboard" in driver.current_url) == expected
