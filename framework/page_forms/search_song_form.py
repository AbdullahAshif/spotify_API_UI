from allure_commons._allure import step
from forms.base_form import BaseForm
from browser.py_quality_services import PyQualityServices
from selenium.webdriver.common.by import By
from resources.locator_constants import LocatorConstants


class SpotifySearchForm(BaseForm):
    __form_name = "Recent searches"

    def __init__(self):
        super(SpotifySearchForm, self).__init__(
            (By.XPATH, LocatorConstants.PRECISE_TEXT_XPATH.format(self.__form_name)), self.__form_name)
        self.__recent_artists_locator = self._element_factory.get_label(
        (By.XPATH, ("//div[@role='button' and contains(@class, 'CardButton-sc-g9vf2u-0')]")), "Recent Artist")

    @step("Checking recent artists name")
    def recent_search(self, artist_name):
        return self.__recent_artists_locator.state.is_displayed
