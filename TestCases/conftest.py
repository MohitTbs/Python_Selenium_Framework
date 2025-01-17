import glob
import os.path
import shutil
from datetime import datetime

import pytest
from selenium import webdriver

from Utilities.creatlog import loggen
from Utilities.util import get_root_of_project


@pytest.fixture(autouse=True)
def setup(browser, request):
    global test_name1
    test_name1 = str(request.node.name)
    global driver
    logger.info("---------" + str(request.node.name) + ": " + "Started--------------------------------")
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
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        logger.error(str(request.node.name) + ": " + "Failed")
        # allure.attach(driver.get_screenshot_as_png(), name=str(request.node.name), attachment_type=AttachmentType.PNG)
    else:
        logger.info(str(request.node.name) + ": " + "Passed")
    if driver is not None:
        driver.close()


def pytest_addoption(parser):  # This will get ṭhe value from CLI /hooks
    parser.addoption("--browser")  # We can pass multiple parameters


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")  # This will return the browser value to setup method


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    now = datetime.now()
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # file_name = report.nodeid.replace("::", "_") + ".png"
            # file_name = "screenshot" + now.strftime("%S%H%d%m%Y") + ".png"
            file_name = "screenshot_" + test_name1 + ".png"
            driver.save_screenshot(os.path.join(get_root_of_project(), 'Reports', file_name))
            # driver.save_screenshot(sys.path[0] + "\\Reports\\" + file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extras = extra
    return report


@pytest.fixture(autouse=True, scope='session')
def setlogs():
    global logger
    logger = loggen()

    # This will delete the entire folder "AllureReports"
    # files = glob.glob(os.path.join('./AllureReports/**'), recursive=True)
    files = glob.glob(os.path.join(get_root_of_project(), 'AllureReports', '**'), recursive=True)
    for f in files:
        # Skip the __init__.py file
        if os.path.basename(f) == '__init__.py':
            continue

        # Check if it is a file or directory
        if os.path.isfile(f):
            os.remove(f)  # Remove files
        elif os.path.isdir(f):
            shutil.rmtree(f)  # Remove directories


# def pytest_exception_interact(node, call, report):
#     if report.failed:
#         test_name = node.name
#         logger.error(f"{test_name} failed:-")
#         # traceback_str = str(call.excinfo.getrepr())
#         # logger.error(traceback_str)

