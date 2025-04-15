from utilities.BaseClass import BaseClass
from pageObjects.LoginFunction import LoginFunction
import time
from testData.TestData import TestData

class TestTwo(BaseClass):

    def test_blankAndInvalidLogin(self):
        log = self.getLogger()
        loginfunction = LoginFunction(self.driver)
        time.sleep(5)
        loginfunction.getsignIn().click()
        log.info("clicking the Login account option without filling details")
        loginfunction.getsecurelogin().click()
        emailmsg = loginfunction.getemailError().text
        assert 'Enter your email' in emailmsg
        log.info("checking assertion errors")
        time.sleep(5)
        pwdmsg = loginfunction.getpwdError().text
        # assert "Enter your password" in pwdmsg

        time.sleep(3)
        log.info("clicking the Login account option with Invalid details")
        td_inavlid=TestData.inavlid_data
        loginfunction.getEmail().send_keys(td_inavlid['email'])
        loginfunction.getPwd().send_keys(td_inavlid['password'])
        time.sleep(5)
        loginfunction.getsecurelogin().click()
        time.sleep(5)
        # act = loginfunction.getsecurelogin()
        # self.getAction(act)
       
        emailmsg = loginfunction.getemailError().text
        assert "Enter valid email for login" in emailmsg
        time.sleep(2)
        log.info("checking assertion errors")
        captchamsg = loginfunction.getcaptchaError().text
        # assert "Enter captcha properly" in captchamsg
        log.info("capturing  assertion errors")
        print(captchamsg)
        loginfunction.getsecurelogin().click()

    def test_forgotPassword(self):
        log = self.getLogger()
        loginfunction = LoginFunction(self.driver)
        loginfunction.getsignIn().click()
        time.sleep(2)
        log.info("clicking the forgot pwd button")
        loginfunction.getforgotPwd().click()
        log.info("sending blank email address")
        loginfunction.getbtnPwd().click()
        #print(loginfunction.getinvalidEmailErr().text)
        ErrMsg=loginfunction.getinvalidEmailErr().text
        if ErrMsg=="Enter your email":
            print("Error msg is present")
        #assert 'Enter your email' in ErrMsg
        time.sleep(2)
        log.info("sending not registered email id")
        td_noRecords=TestData.no_records
        loginfunction.getforgotEmail().send_keys(td_noRecords['email'])
        loginfunction.getbtnPwd().click()
        ErrMsgOne=loginfunction.getinvalidEmailErr().text
        print(ErrMsgOne)
        #assert "No customer records found." in ErrMsgOne
        time.sleep(2)
        log.info("sending valid email id")
        td_valid=TestData.test_Data
        loginfunction.getforgotEmail().clear()
        loginfunction.getforgotEmail().send_keys(td_valid['email'])
        loginfunction.getbtnPwd().click()
        ErrMsgtwo=loginfunction.getinvalidEmailErr().text
        print(ErrMsgtwo)
        #assert "Your password has been sent to you" in ErrMsgtwo
        loginfunction.getclosePwdForm().click()


    def test_validLogin(self):
        log = self.getLogger()
        loginfunction = LoginFunction(self.driver)
        self.login()
        time.sleep(5)
        # loginfunction.getsignIn().click()
        # log.info("clicking the Login account option with valid details")
        # loginfunction.getsecurelogin().click()
        # time.sleep(5)
        loginfunction.getLogout().click()
