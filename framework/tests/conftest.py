import allure
import pytest
from framework.utils.spotify_search import SpotifyApiSearch
from framework.utils.browser_factory import BrowserFactory
from browser.py_quality_services import PyQualityServices
from framework.utils.settings_data import SettingsData


def pytest_sessionstart(session):
    PyQualityServices.browser_factory = BrowserFactory()
    PyQualityServices.get_browser()


@allure.feature("Setting up Browser")
@pytest.fixture(scope="session", autouse=True)
def browser(request):
    with allure.step("Opening Browser"):
        driver = PyQualityServices.get_browser()
    with allure.step("Maximizing Browser"):
        driver.maximize()
    with allure.step("GoTo URL"):
        driver.go_to(SettingsData.get_env_data()['host'])
    driver.wait_for_page_to_load()
    yield driver
    with allure.step("Terminating Browser"):
        driver.quit()


@pytest.fixture(scope="session")
def spotify_api_client():
    return SpotifyApiSearch()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if 'ui' in item.keywords and report.when == "call":  # Check if the test is marked as UI
        browser = item.funcargs.get('browser')
        if browser:
            screenshot_name = "screenshot_on_failure" if report.failed else "screenshot_on_success"
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
