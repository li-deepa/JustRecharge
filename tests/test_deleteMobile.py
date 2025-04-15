from utilities.BaseClass import BaseClass
from pageObjects.DeleteMobile import DeleteMobile
import time


class TestFive(BaseClass):

    def test_DelteMobileNo(self):
        try:
            log = self.getLogger()
            self.login()
            time.sleep(5)
            self.driver.refresh
            deletefunction= DeleteMobile(self.driver)
            time.sleep(5)
            delete = deletefunction.getdelete()
            self.actionRandom(delete)
            time.sleep(3)
            alert = self.driver.switch_to.alert
            time.sleep(5)
            alert.dismiss()
            time.sleep(5)
            deleteone = deletefunction.getdelete()
            self.actionRandom(deleteone)
            time.sleep(5)
            alert = self.driver.switch_to.alert
            time.sleep(5)
            alert.accept()
            time.sleep(5)
        except Exception as E:
            print("no mobile numbers to delete")