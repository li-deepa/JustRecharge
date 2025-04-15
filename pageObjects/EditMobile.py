from selenium.webdriver.common.by import By

class EditMobile:

    def __init__(self,driver):
        self.driver = driver
      
    editBtn = (By.XPATH,"//img[@id='listingtable_btnGridEdit_0']")
    
    
    cancelBtn = (By.XPATH,'//table[@id="listingtable"]//td[7]//a[2]')

    update=(By.XPATH,"//*[@class='textfield-98x28 radius']")
    save=(By.XPATH,"//*[@title='Save']")

    def getEdit(self):
        return self.driver.find_element(*EditMobile.editBtn)

    def getCancel(self):
        return self.driver.find_element(*EditMobile.cancelBtn)

    def getupdate(self):
        return self.driver.find_element(*EditMobile.update)

    def getSave(self):
        return self.driver.find_element(*EditMobile.save)
