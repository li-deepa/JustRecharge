from utilities.BaseClass import BaseClass
from pageObjects.EditMobile import EditMobile
from selenium.webdriver.support.wait import WebDriverWait
import time


class TestFour(BaseClass):

    def test_EditMobileNo(self):
        log = self.getLogger()
        time.sleep(5)
        self.login()
        time.sleep(5)
        # self.driver.refresh
        editfunction = EditMobile(self.driver)
        time.sleep(5)
        log.info("clicking the Edit Button ")
        edit = editfunction.getEdit()
        #self.actionRandom(edit)
        edit.click()
        time.sleep(5)
        log.info("clicked the Edit Button  option and updating details")
        editfunction.getupdate().clear()
        WebDriverWait(self.driver,10)
        editfunction.getupdate().send_keys("9090912345")
        editfunction.getCancel().click()
        log.info("cancel the update number")
        # alert = self.driver.switch_to.alert
        # time.sleep(5)
        # if alert ==True:
        #     alert.dismiss()
        time.sleep(5)
        editone = editfunction.getEdit()
        editone.click()
        log.info("clicked the Edit Button  option and updating details")
        editfunction.getupdate().clear()
        WebDriverWait(self.driver,5)
        editfunction.getupdate().send_keys("9677182054")
        log.info("updated  the phone number")
        time.sleep(5)
        editfunction.getSave().click()
        time.sleep(5)