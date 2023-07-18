from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        service = Service(executable_path='C:/Users/A4003/PycharmProjects/pythonProject/drivers/chromedriver.exe')
        driver = webdriver.Chrome(service=service)
        print("Launching chrome browser---------------")
    elif browser == 'edge':
        service = Service(executable_path='C:/Users/A4003/PycharmProjects/pythonProject/drivers/msedgedriver.exe')
        driver = webdriver.Edge(service=service)
        print("Launching edge browser---------------")
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#######################pytest html report ###########################
# it hooks for adding environment info to html report
def pytest_configure(config):
    config._metadata = {
        "Tester": "Rishabh",
        "Project Name": "Python Framework Practice",
    }


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugin", None)
