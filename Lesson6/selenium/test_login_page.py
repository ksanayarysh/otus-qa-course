import pytest

@pytest.mark.login_with_different_creds
@pytest.mark.usefixtures("login")
class TestLoginPage:

    @pytest.mark.usefixtures("login")
    @pytest.mark.parametrize("user,password,expected", [
        pytest.param("admin", "11", False, id='wrong'),
        pytest.param("test1", "\\t", False, id='wrong'),
        pytest.param("  ", "123", False, id='wrong'),
        pytest.param("john", "wee", False, id='wrong')
#         pytest.param("admin", "admin", True, id='right'),
    ])
    def test_login(self, driver, user, password, expected):
        assert ("Dashboard".lower() in driver.title.lower()) == expected
