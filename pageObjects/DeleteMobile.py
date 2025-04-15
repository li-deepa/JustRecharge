from selenium.webdriver.common.by import By


class DeleteMobile:

    def __init__(self,driver):
        self.driver = driver

    deletebtn = (By.XPATH,"//*[@title='Delete']")


    def getdelete(self):
        return self.driver.find_elements(*DeleteMobile.deletebtn)

