import pytest
from browser.py_quality_services import PyQualityServices
from framework.utils.browser_factory import BrowserFactory


def pytest_sessionstart(session):
    PyQualityServices.browser_factory = BrowserFactory()
    PyQualityServices.get_browser()
