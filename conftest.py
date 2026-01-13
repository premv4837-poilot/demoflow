import pytest
from selenium import webdriver

driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Browser name: chrome or firefox"
    )

@pytest.fixture(scope="function")
def broswerInstance(request):
    global  driver
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser_name == "firefox":
        driver = webdriver.firefox()
        driver.maximize_window
    yield driver


import pytest
import os

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)
            screenshot_path = os.path.join(
                screenshots_dir, f"{item.name}.png"
            )
            driver.save_screenshot(screenshot_path)


