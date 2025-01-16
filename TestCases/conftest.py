import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def setup(browser, request):
    global driver
    # LogGen.static_logger.info("---------" + str(request.node.name) + ": " + "Started--------------------------------")
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
    print('Driver Initiated')
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver


@pytest.fixture(autouse=True)
def tear_down(request):
    yield
    if driver is not None:
        driver.close()


def pytest_addoption(parser):  # This will get ṭhe value from CLI /hooks
    parser.addoption("--browser")  # We can pass multiple parameters


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")  # This will return the browser value to setup method
