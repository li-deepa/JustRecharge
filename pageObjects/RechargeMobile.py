from selenium.webdriver.common.by import By

class RechargeMobile:

    def __init__(self,driver):
        self.driver = driver

    myaccount=(By.XPATH,"//a[contains(text(),'My Account')]")
    directory= (By.XPATH,'//*[@class="hyLink2"]')
    recharge= (By.XPATH,'//*[@class="hyLink1"]')
    btnProceed= (By.ID,"btnProceedtoPay")
    rechargeErr=(By.CSS_SELECTOR,"#lblErrorMsgRechargeAmt")
    rechargeAmt =(By.XPATH,"//*[@class='textfield-165x33 radius rupee']")
    selectJri= (By.XPATH,"//span[@id='lblUserJriCard']")
    paymentErr=(By.ID,"lblErrorMsgJriCard")
    selectDebit =(By.ID,"lblUserDebitCard")
    clickMaestro=(By.XPATH,"//span[@id='lstvDebit2_ctrl2_lblPaymentGname_5']")
    debitCardNo=(By.ID,"debitCardNumber")
    selectExpMonth= (By.ID,"expiryMonthDebitCard")
    selectExpYear= (By.XPATH,'//*[@id="expiryYearDebitCard"]')
    cvvNo =(By.ID,"CVVNumberDebitCard")
    makePaymentBtn=(By.ID,"SubmitBillShip")
    cancelBtn =(By.XPATH,"//a[@class='primary-button primary-button-bg cancel']")
    cardsError=(By.XPATH,"//*[@class='error']")
    contPayment=(By.XPATH,"//*[@title='Continue Payment']")
    cancenTran =(By.XPATH,"//*[@title='Cancel Transaction']")
    tranFailed=(By.CLASS_NAME,"icon_failed")
    payAgain=(By.XPATH,"//a[@id='lnkPayAgain']//img")
    myProfile=(By.XPATH,"//*[@id='myprofile_tab']")
    tranHistory=(By.XPATH,"//*[@id='transactionhistory_tab']")
    tranRow=(By.XPATH,"//*[@class='listrow'][1]")
    ServiceProvider=(By.ID,"lblUserTxt1")


    def getdirectory(self):
        return self.driver.find_element(*RechargeMobile.directory)

    def getaccount(self):
        return self.driver.find_elements(*RechargeMobile.myaccount)

    def getServiceProvider(self):
        return self.driver.find_element(*RechargeMobile.ServiceProvider)

    def getRecharge(self):
        return self.driver.find_elements(*RechargeMobile.recharge)

    def getbtnProceed(self):
        return self.driver.find_element(*RechargeMobile.btnProceed)

    def getrechargeErr(self):
        return self.driver.find_element(*RechargeMobile.rechargeErr)

    def getrechargeAmt(self):
        return self.driver.find_element(*RechargeMobile.rechargeAmt)

    def getselectJri(self):
        return self.driver.find_element(*RechargeMobile.selectJri)

    def getpaymentErr(self):
        return self.driver.find_element(*RechargeMobile.paymentErr)

    def getselectDebit(self):
        return self.driver.find_element(*RechargeMobile.selectDebit)

    def getclickMaestro(self):
        return self.driver.find_element(*RechargeMobile.clickMaestro)

    def getdebitCardNo(self):
        return self.driver.find_element(*RechargeMobile.debitCardNo)

    def getselectExpDate(self):
        return self.driver.find_element(*RechargeMobile.selectExpMonth)

    def getselectExpYear(self):
        return self.driver.find_element(*RechargeMobile.selectExpYear)

    def getcvvNo(self):
        return self.driver.find_element(*RechargeMobile.cvvNo)

    def getmakePaymentBtn(self):
        return self.driver.find_element(*RechargeMobile.makePaymentBtn)

    def getcancelBtn(self):
        return self.driver.find_element(*RechargeMobile.cancelBtn)

    def getcardsErr(self):
        return self.driver.find_elements(*RechargeMobile.cardsError)

    def getcontPayment(self):
        return self.driver.find_element(*RechargeMobile.contPayment)

    def getcancenTran(self):
        return self.driver.find_element(*RechargeMobile.cancenTran)

    def gettranFailed(self):
        return self.driver.find_elements(*RechargeMobile.tranFailed)

    def getpayAgain(self):
        return self.driver.find_elements(*RechargeMobile.payAgain)

    def getmyProfile(self):
        return self.driver.find_element(*RechargeMobile.myProfile)

    def gettranHistory(self):
        return self.driver.find_element(*RechargeMobile.tranHistory)

    def gettranRow(self):
        return self.driver.find_element(*RechargeMobile.tranRow)