"""Download page"""
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Lesson6.selenium.models.page import BasePage
from Lesson6.selenium.models.locator import DownloadFileLocators


class DownloadPage(BasePage):
    """Class for using download page"""
    def set_download_name(self, name):
        """Setting name for a download"""
        download_input = self.driver.find_element(*DownloadFileLocators.DOWNLOAD_FILE_NAME)
        self._clear_element_(download_input)
        download_input.send_keys(name)

    def upload_file(self):
        """Uploading file"""
        upload_button = self.driver.find_element(*DownloadFileLocators.UPLOAD_BUTTON)
        upload_button.click()
        file_input = self.driver.find_elements(*DownloadFileLocators.FILE)
        if file_input:
            dirname = os.path.dirname(__file__)
            filename = os.path.join(dirname, "pylint.png")
            file_input[0].send_keys(filename)
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert.accept()
            save_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(DownloadFileLocators.SAVE_BUTTON))
            save_button.click()
        assert file_input

    def get_download_count(self):
        """Getting current count of download files"""
        downloads = self.driver.find_elements(*DownloadFileLocators.DOWNLOADS)
        return len(downloads)

    def add_download_button_press(self):
        """Pressing add button"""
        self.driver.find_element(*DownloadFileLocators.ADD_BUTTON).click()
