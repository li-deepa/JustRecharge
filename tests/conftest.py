import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
from selenium import webdriver
import pyautogui
import time

# def record_screen():
#     for i in range(100):  # Capture 100 frames
#         pyautogui.screenshot(f"frame_{i}.png")
#         time.sleep(0.1)  # Capture every 0.1 seconds
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    
    browser_name == "chrome"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    

    url = "https://www.justrechargeit.com/"
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     Extends the PyTest Plugin to take and embed screenshots in the HTML report whenever a test fails.
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])

#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = (
#                     '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '
#                     'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 )
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra

# def _capture_screenshot(file_name):
#     """
#     Captures a screenshot and saves it with the given file name.
#     """
#     driver.get_screenshot_as_file(file_name)