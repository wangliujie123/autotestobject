import sys
sys.path.append("../page_object")
from base.base import  Base
from selenium.webdriver.common.by import By
import  time,os,pytest
from pageobject import fateadm_api
from selenium import webdriver
import pytest_check as check


class LoginPage(Base):

    login_user = "xpath", "//input[@placeholder='账号']"
    
    login_password = "xpath", "//input[@placeholder='密码']"
    
    login_validateCode = "xpath", "//input[@placeholder='验证码']"

    testname = "xpath", "//*[@id='app']/div/div[1]/div[3]/div/div[2]"
    
    def login_validateImage(self):
        return self.findele(By.CLASS_NAME,'login-code')
    #login_validateImage = "classname",'login-code'

    login_button = "xpath", "//span[text()='登录']/ancestor::button"
    
    def login_system(self,username='admin',password='HM_2023_test'):
        #filename = "capture.png"
        #if os.path.exists(filename):
        #    os.remove(filename)
        #self.login_validateImage().screenshot(filename)
        self.send(self.login_user,username)
        self.send(self.login_password,password)
        self.send(self.login_validateCode,'2')
        time.sleep(5)
        #verification_code = str(fateadm_api.TestFunc())
        #self.send(self.login_validateCode,verification_code)
        self.clickbtn(self.login_button)
        time.sleep(3)
        testname = self.gettext(self.testname)
        print(testname)
        return testname

if __name__ == '__main__':
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('http://kdtx-test.itheima.net/')
    LoginPage(driver).login_system()

