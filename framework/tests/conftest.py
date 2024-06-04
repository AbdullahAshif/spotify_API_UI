import pytest
from framework.utils.spotify_search import SpotifyApiSearch
from framework.utils.browser_factory import BrowserFactory
from browser.py_quality_services import PyQualityServices
from framework.utils.settings_data import SettingsData


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    driver = PyQualityServices.get_browser()
    driver.maximize()
    driver.go_to(SettingsData.get_env_data()['host'])
    driver.wait_for_page_to_load()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def spotify_api_client():
    return SpotifyApiSearch()

def pytest_sessionstart(session):
    PyQualityServices.browser_factory = BrowserFactory()
    PyQualityServices.get_browser()
