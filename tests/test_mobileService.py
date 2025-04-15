from utilities.BaseClass import BaseClass
from pageObjects.LoginFunction import LoginFunction
from pageObjects.MobileService import MobileService
from testData.TestData import TestData
import pytest
import time


class TestThree(BaseClass):

    @pytest.mark.skipif(reason='ElementNotInteractableException')
    def test_invalidandValidMobiledata(self):
        log = self.getLogger()
        time.sleep(5)
        self.login()
        # self.driver.refresh
        time.sleep(5)
        mobilefunction = MobileService(self.driver)
        log.info("checking mobile service is enabled or not")
        check = mobilefunction.getmobileService()
        self.getAction(check)
        time.sleep(5)
        log.info("adding mobile service with  blank data")
        mobilefunction.getmobileNo().clear()
        time.sleep(5)
        mobilefunction.getmobileAdd().click()
        msg = mobilefunction.getmobileErr().text
        if msg == "Enter mobile number":
            print("its true")
        self.driver.refresh
        time.sleep(2)
        log.info("adding mobile service with  invalid data")
        mobilefunction.getmobileNo().send_keys("1234567890")
        mobilefunction.getmobileAdd().click()
        msg2 = mobilefunction.getmobileErr().text
        time.sleep(5)
        if msg2 == "Enter valid mobile number":
            print(msg2)
        time.sleep(2)
        mobilefunction.getmobileNo().clear()
        mobilefunction.getmobileNo().send_keys("9618407971")
        log.info("adding mobile service with  valid data")
        time.sleep(5)
        mobilefunction.getmobileAdd().click()
        time.sleep(2)
        self.driver.refresh
        mobilefunction = LoginFunction(self.driver)
        mobilefunction.getLogout().click()

    def test_addMobileNo(self):
        log = self.getLogger()
        time.sleep(10)
        self.login()
        time.sleep(10)
        log.info("login")
        # self.driver.refresh
        # log.info("changing driver by refreshing")
        mobilefunction = MobileService(self.driver)
       
        log.info("Adding 10 mobile numbers")
        list = TestData.listofMobiles
        elem = len(list)
        time.sleep(5)
        for i in range(0,elem):
            mobilefunction.getmobileAdd().click()
            log.info("clicking the mobile option to add numbers")
            time.sleep(5)
            mobilefunction.getaddMobileNo().send_keys(list[i])
            log.info("adding numbers")

            time.sleep(5)
            log.info("clicking the mobile option and adding numbers")

            mobilefunction.getaddBtn().click()
            time.sleep(5)
            for x in range(10):
                log.info(f"added{x}")

            if mobilefunction.getmobileExist().text == "Mobile number already exists":
                mobilefunction.getbtnCancel().click()
                continue
            if mobilefunction.getmobileExist().text == "You can not add more than 10 mobile numbers to your account":
                break
        time.sleep(5)
