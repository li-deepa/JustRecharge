
from selenium.webdriver.common.by import By


class MobileService:

    def __init__(self,driver):
        self.driver = driver

    mobile=(By.CSS_SELECTOR,"#imgMobile")
    mobileNo=(By.ID,"txtMobileNo")
    mobileAdd=(By.ID,"hidClickAddBtnInViewPanel")
    # mobileAdd=(By.XPATH,"//*[@id='divLnkAddMobile']/a")
    # //*[@id="divLnkAddMobile"]/a

    mobileErr = (By.ID,"errorMsgMobile")
    addMobile=(By.CLASS_NAME,"addMobileLink")
    addMobileNo=(By.ID,"txtpopMobileNo")
    addBtn = (By.ID,"btnPopupAddMobile")
    mobileLocation=(By.ID,"ddlMobileServiceProviderLocation")
    mobileExists=(By.ID,"lblpopMobileErrorMsg")
    btnCancel=(By.XPATH,"//input[@id='img1']")
    myaccount=(By.XPATH,"//a[contains(text(),'My Account')]")
    directory= (By.XPATH,'//*[@class="hyLink2"]')


    def getaddMobileNo(self):
        return self.driver.find_element(*MobileService.addMobileNo)

    def getmobileService(self):
        return self.driver.find_element(*MobileService.mobile)

    def getmobileNo(self):
        return self.driver.find_element(*MobileService.mobileNo)

    def getmobileAdd(self):
        return self.driver.find_element(*MobileService.mobileAdd)

    def getmobileErr(self):
        return self.driver.find_element(*MobileService.mobileErr)

    def getaddMobileNo(self):
        return self.driver.find_element(*MobileService.addMobileNo)
    
    def getdirectory(self):
        return self.driver.find_element(*MobileService.directory)

    def getaccount(self):
        return self.driver.find_elements(*MobileService.myaccount)


    def getmobileFunction(self):
        return self.driver.find_element(*MobileService.mobileLocation)

    def getaddBtn(self):
        return self.driver.find_element(*MobileService.addBtn)

    def getmobileExist(self):
        return self.driver.find_element(*MobileService.mobileExists)

    def getbtnCancel(self):
        return self.driver.find_element(*MobileService.btnCancel)

