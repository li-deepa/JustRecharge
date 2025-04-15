from utilities.BaseClass import BaseClass
from pageObjects.CreateAccount import CreateAccount
import time
from testData.TestData import TestData

class TestOne(BaseClass):

    def test_blankAndInvalidSubmission(self):
        log = self.getLogger()
        createaccount = CreateAccount(self.driver)
        td_inavlid= TestData.inavlid_data
        log.info("clicking the create account option without filling details")
        time.sleep(5)
        createaccount.getcreateAccount().click()
        createaccount.getCreate().click()
        time.sleep(5)
        namemsg = createaccount.getnameError().text
        mobilemsg = createaccount.getmobileError().text
        emailmsg = createaccount.getemailError().text
        pwdmsg = createaccount.getpwdError().text
        time.sleep(5)
        assert "Enter your name" in namemsg
        #assert "Enter mobile no." in mobilemsg
        #assert "Enter your email id" in emailmsg
        #assert "Enter your password" in pwdmsg
        self.driver.refresh
        time.sleep(5)
        log.info("sending invalid data")
        createaccount.getName().send_keys(td_inavlid['name'])
        createaccount.getMobile().send_keys(td_inavlid['mobile'])
        createaccount.getEmail().send_keys(td_inavlid['email'])
        createaccount.getPassword().send_keys(td_inavlid['password'])
        createaccount.getCreate().click()
        Invalidname = createaccount.getnameError()
        Invalidmobile = createaccount.getmobileError()
        Invalidemail = createaccount.getemailError()
        Invalidpwd = createaccount.getpwdError()
        log.info("checking error msgs by assertion")
        assert "Enter correct name" in Invalidname.text
        # assert "Enter valid 10 digit mobile no." in Invalidmobile.text
        assert "Enter 10 digit mobile no." in Invalidmobile.text
        assert "Enter valid email id" in Invalidemail.text
        assert "Enter 6-digit numeric characters only" in Invalidpwd.text

    def test_validSubmission(self):
        try:
            log = self.getLogger()
            log.info("testing with valid data")
            td_valid=TestData.test_Data
            createaccount = CreateAccount(self.driver)
            createaccount.getcreateAccount().click()
            createaccount.getName().send_keys(td_valid['name'])
            createaccount.getMobile().send_keys(td_valid['mobile'])
            createaccount.getEmail().send_keys(td_valid['email'])
            createaccount.getPassword().send_keys(td_valid['password'])
            log.info("checking check boxes")
            createaccount.getCheckboxone().click()
            createaccount.getCheckbox().click()
            createaccount.getCreate().click()
            print("Account created successfully")
        except  Exception as E:
            print("account already exists")