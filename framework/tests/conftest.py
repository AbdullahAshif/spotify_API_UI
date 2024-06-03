import pytest
from browser.py_quality_services import PyQualityServices
from framework.utils.browser_factory import BrowserFactory
from framework.utils.spotify_search import SpotifyApiSearch


@pytest.fixture(scope="session")
def spotify_api_client():
    return SpotifyApiSearch()


def pytest_sessionstart(session):
    PyQualityServices.browser_factory = BrowserFactory()
    PyQualityServices.get_browser()
