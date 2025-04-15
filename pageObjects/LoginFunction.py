from selenium.webdriver.common.by import By


class LoginFunction:

    def __init__(self,driver):
        self.driver = driver

    login = (By.XPATH,"//a[@id='jriTop_signin9']")
    email = (By.ID,"txtUserName")
    pwd = (By.ID,"txtPasswd")
    captcha = (By.XPATH,"//span[@id='ucCaptcha']//img")
    txtcaptcha = (By.ID,"txtCaptcha")
    secureLogin=(By.XPATH,"//*[@id='imgbtnSignin']")
    emailError=(By.CSS_SELECTOR,"#MessageCaption2")
    pwdError=(By.CSS_SELECTOR,"#MessageCaption3")
    captchaError=(By.XPATH,"//span[@id='MessageCaption4']")
    forgotPwd =(By.CSS_SELECTOR,"#forgotpassword")
    forgotEmail = (By.XPATH,"//input[@id='forgotpass_txtEmailId']")
    btnPwd=(By.XPATH,"//input[@id='forgotpass_imgbtnSubmit']")
    emailNotFound=(By.ID,'forgotpass_lblError')
    #pwdSent = (By.XPATH,"//span[@id='forgotpass_lblError']")
    logout=(By.CSS_SELECTOR,"#jriTop_signOut")
    closePwdForm=(By.XPATH,"//div[@id='forgotpasswordform']//span[@class='close-link']")

    def getsignIn(self):
        return self.driver.find_element(*LoginFunction.login)

    def getEmail(self):
        return self.driver.find_element(*LoginFunction.email)

    def getPwd(self):
        return self.driver.find_element(*LoginFunction.pwd)

    def getcaptcha(self):
        return self.driver.find_element(*LoginFunction.captcha)

    def gettxtcaptcha(self):
        return self.driver.find_element(*LoginFunction.txtcaptcha)

    def getsecurelogin(self):
        return self.driver.find_element(*LoginFunction.secureLogin)

    def getemailError(self):
        return self.driver.find_element(*LoginFunction.emailError)

    def getpwdError(self):
        return self.driver.find_element(*LoginFunction.pwdError)

    def getcaptchaError(self):
        return self.driver.find_element(*LoginFunction.captchaError)

    def getforgotPwd(self):
        return self.driver.find_element(*LoginFunction.forgotPwd)

    def getforgotEmail(self):
        return self.driver.find_element(*LoginFunction.forgotEmail)

    def getbtnPwd(self):
        return self.driver.find_element(*LoginFunction.btnPwd)

    def getinvalidEmailErr(self):
        return self.driver.find_element(*LoginFunction.emailNotFound)

    def getLogout(self):
        return self.driver.find_element(*LoginFunction.logout)

    def getclosePwdForm(self):
        return self.driver.find_element(*LoginFunction.closePwdForm)

   # def getpwdSent(self):
      #  return self.driver.find_element(*LoginFunction.pwdSent)





