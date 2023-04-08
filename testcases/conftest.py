import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request, browser, url):
    global driver
    if browser == "chrome": driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")


def pytest_html_report_title(report):
    report.title = "Swag Labs Automation Report"
