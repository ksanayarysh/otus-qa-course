"""Module for testing of downloading file"""
import allure
import pytest


@pytest.mark.usefixtures("download_page")
@pytest.mark.usefixtures("open_product_page")
@pytest.mark.usefixtures("login")
@pytest.mark.parametrize("user,password", [("admin", "admin")])
@pytest.mark.usefixtures("open_login_page")
@allure.title("Test download")
class TestDownloadFile:
    """Class for tests downloading file"""
    @pytest.mark.xfail(reason="Not yet implemented")
    def test_download_file(self, download_page):
        """
        Gets current count of downloads, adds a new one,
        gets new count and checks if new count equals old + 1
        """
        current_downloads = download_page.get_download_count()
        download_page.add_download_button_press()
        download_page.set_download_name("file_name")
        download_page.upload_file()
        new_downloads = download_page.get_download_count()
        assert new_downloads == current_downloads + 1
