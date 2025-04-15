from utilities.BaseClass import BaseClass
from pageObjects.LoginFunction import LoginFunction
from pageObjects.RechargeMobile import RechargeMobile
from selenium.webdriver import ActionChains
import random
from testData.TestData import TestData
import time

class TestSix(BaseClass):

    def test_rechargeMobile(self):
        log = self.getLogger()
        self.login()
        time.sleep(2)
        # self.driver.refresh
        # log.info("changing driver by refreshing")
        rechargemobile = RechargeMobile(self.driver)
        # rechargemobile.getaccount().click()
        # rechargemobile.getdirectory().click()
        recharge=rechargemobile.getRecharge()
        time.sleep(5)
        elem= (len(recharge)-1)
        rand = random.randint(0,elem)
        log.info("randomly selecting a number")
        Action = ActionChains(self.driver)
        time.sleep(5)
        act =Action.move_to_element(recharge[rand])
        time.sleep(2)
        act.click().perform()
        time.sleep(5)
        rechargemobile.getbtnProceed().click()
        err=rechargemobile.getrechargeErr().text
        if "Enter recharge amount" in err:
            print("Enter recharge amount")
        time.sleep(5)
        print(rechargemobile.getServiceProvider().text)
        rechargemobile.getrechargeAmt().send_keys("50")
        rechargemobile.getbtnProceed().click()
        log.info("selecting Jri recharge option to pay")
        rechargemobile.getselectJri().click()
        rechargemobile.getbtnProceed().click()
        Err=rechargemobile.getpaymentErr().text
        if "You don't have sufficient funds available in your JRI card" in Err:
            print("You don't have sufficient funds available")
        time.sleep(2)
        log.info("selecting debit card  option to pay")
        rechargemobile.getselectDebit().click()
        time.sleep(3)
        rechargemobile.getclickMaestro().click()
        rechargemobile.getbtnProceed().click()
        time.sleep(10)
        rechargemobile.getmakePaymentBtn().click()
        cardsErrors=str(rechargemobile.getcardsErr()).strip("[").strip("]")
        if "Please enter card number." in  cardsErrors:
            print("Please enter card number.")
        time.sleep(5)
        log.info("sending invalid  debit card  details to pay")
        td_invalid=TestData.debit_InvaildDetails
        rechargemobile.getdebitCardNo().send_keys(td_invalid['cardno'])
        self.selectOptionByText(rechargemobile.getselectExpDate(),td_invalid['month'])
        self.selectOptionByText(rechargemobile.getselectExpYear(),td_invalid['year'])
        rechargemobile.getcvvNo().send_keys(td_invalid['cvv'])
        rechargemobile.getmakePaymentBtn().click()
        if "Please enter valid card number." in cardsErrors:
            print("Please enter valid card number.")
        time.sleep(5)
        self.driver.back()
        rechargemobile.getrechargeAmt().send_keys("50")
        rechargemobile.getbtnProceed().click()
        time.sleep(2)
        rechargemobile.getselectDebit().click()
        time.sleep(3)
        rechargemobile.getclickMaestro().click()
        rechargemobile.getbtnProceed().click()
        time.sleep(10)
        log.info("sending valid  debit card  details to pay")
        td_valid=TestData.debit_vaildDetails
        rechargemobile.getdebitCardNo().send_keys(td_valid['cardno'])
        self.selectOptionByText(rechargemobile.getselectExpDate(),td_valid['month'])
        self.selectOptionByText(rechargemobile.getselectExpYear(),td_valid['year'])
        rechargemobile.getcvvNo().send_keys(td_valid['cvv'])
        rechargemobile.getcancelBtn().click()
        time.sleep(2)
        rechargemobile.getcancenTran().click()
        time.sleep(5)


    def test_validTrans(self):
        log = self.getLogger()
        self.login()
        # self.driver.refresh
        log.info("changing driver by refreshing")
        rechargemobile = RechargeMobile(self.driver)
        rechargemobile.getmyProfile().click()
        rechargemobile.gettranHistory().click()
        print(rechargemobile.gettranRow().text)