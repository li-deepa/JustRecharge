from selenium.webdriver.common.by import By

class CreateAccount:

    def __init__(self,driver):
        self.driver = driver

    createAccount = (By.ID,"signup-link9")
    name = (By.XPATH, '//*[@id="signup_name"]')
    mobile = (By.XPATH, '//*[@id="signup_mobileno"]')
    email = (By.XPATH, '//*[@id="signup_email"]')
    password =(By.XPATH, '//*[@id="signup_password"]')
    checkbox =(By.ID,"checkbox")
    checkboxone = (By.ID,"checkbox1")
    create = (By.ID,"imgbtnSubmit")

    # nameErrorMsg = (By.XPATH,"//td[@id='nameTD']']")

    nameerrorMsg = (By.XPATH,"//td[@id='nameTD']")
    mobileerrorMsg = (By.XPATH,"//td[@id='mobilenoTD']")
    emailerrorMsg = (By.XPATH,"//td[@id='emailTD']")
    passworderrorMsg = (By.XPATH,"//td[@id='passwordTD']")
    invalidErrors= (By.CLASS_NAME,"errormsg")


    def getcreateAccount(self):
        return self.driver.find_element(*CreateAccount.createAccount)

    def getName(self):
        return self.driver.find_element(*CreateAccount.name)

    def getMobile(self):
        return self.driver.find_element(*CreateAccount.mobile)

    def getEmail(self):
        return self.driver.find_element(*CreateAccount.email)

    def getPassword(self):
        return self.driver.find_element(*CreateAccount.password)

    def getCheckbox(self):
        return self.driver.find_element(*CreateAccount.checkbox)

    def getCheckboxone(self):
        return self.driver.find_element(*CreateAccount.checkboxone)

    def getCreate(self):
        return self.driver.find_element(*CreateAccount.create)

    def getnameError(self):
        return self.driver.find_element(*CreateAccount.nameerrorMsg)

    def getmobileError(self):
        return self.driver.find_element(*CreateAccount.mobileerrorMsg)

    def getemailError(self):
        return self.driver.find_element(*CreateAccount.emailerrorMsg)

    def getpwdError(self):
        return self.driver.find_element(*CreateAccount.passworderrorMsg)

    def getInavlidmsgs(self):
        return self.driver.find_element(*CreateAccount.invalidErrors)



