import pytest
from browser.py_quality_services import PyQualityServices
from framework.utils.settings_data import SettingsData


@pytest.fixture(scope="session", autouse=True)
def prepare_browser_factory(request):
    driver = PyQualityServices.get_browser()
    driver.maximize()
    driver.go_to(SettingsData.get_env_data()['host'])
    driver.wait_for_page_to_load()
    yield driver
    driver.quit()
