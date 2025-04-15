import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import logging
import inspect
import pytesseract
from PIL import Image
from io import BytesIO
from selenium.webdriver import ActionChains
import random
import time
from testData.TestData import TestData
from pageObjects.LoginFunction import LoginFunction
import  os

# def open_screenshot():
#     ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
#     screenshotpath = os.path.join(os.path.sep, ROOT_DIR,)
#     # print (screenshotpath)
#     return screenshotpath

@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)  # file handler object

        logger.setLevel(logging.DEBUG)
        return logger

    @pytest.mark.usefixtures(scope="class")
    def getcaptcha(self,captch):
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        screenshotpath = os.path.join(os.path.sep, ROOT_DIR,)
        im = Image.open(BytesIO(captch))
        im.save(screenshotpath+r'/cap.png')
        pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
        image = Image.open(screenshotpath+r'/cap.png',mode='r')
        result = pytesseract.image_to_string(image)
        with open('abc.txt',mode='w') as file:
            file.write(result)
        self.driver.implicitly_wait(4)
        files = open('abc.txt')
        str = files.read().replace("=",'')
        str = str.replace("+",',').split(',')
        st = int(str[0]) + int(str[1])
        # st=int(eval(str))
        return st
        # print(st)

    def getAction(self,act):
        action=ActionChains(self.driver)
        action.double_click(act).perform()


    def getRandom(self):
        random_list = []
        for i in range(1,11):
            rand =random.randint(9000000000,9999999999)
            random_list.append(rand)
        return random_list


    def getActSend(self,send):
        action = ActionChains(self.driver)
        action.send_keys(send).perform()

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def verifyLink(self,locator):
        wait = WebDriverWait(self.driver,8).until(
            EC.element_to_be_clickable(locator))

    def actionRandom(self,locator):
        elem = (len(locator))
        rand = random.randint(0,elem)
        Action = ActionChains(self.driver)
        act = Action.move_to_element(locator[rand])
        time.sleep(5)
        act.click().perform()

    def login(self):
        log = self.getLogger()
        loginfunction = LoginFunction(self.driver)
        td_valid=TestData.test_Data
        log.info("clicking the Login account option with valid details")
        loginfunction.getsignIn().click()
        loginfunction.getEmail().send_keys(td_valid["email"])
        loginfunction.getPwd().send_keys(td_valid["password"])
        time.sleep(5)
        st = self.getcaptcha(loginfunction.getcaptcha().screenshot_as_png)
        loginfunction.gettxtcaptcha().send_keys(st)
        loginfunction.getsecurelogin().click()