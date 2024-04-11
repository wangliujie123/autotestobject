import sys
sys.path.append("../page_object")
from lxml import etree
from bs4 import BeautifulSoup
import requests,time,pytest
from base.base import  Base
from selenium.webdriver.common.by import By
from selenium import webdriver
from pageobject.login_page import LoginPage




class CoursePage(Base):

    course_model = "xpath", "//a[@href='#/course']"

    course_name = "xpath", "//input[@placeholder='请输入课程名称']"

    course_search = "xpath", "//span[text()='搜索']/parent::button"
    
    course_update_btn = "xpath", "//span[text()='修改']/parent::button"

    course_add_button = "xpath", "//span[text()='添加课程']/parent::button"

    window_course_subject = "xpath", "//div/following-sibling::div/form/descendant::input[@placeholder='请选择课程学科']"

    window_course_name = "xpath", "//div/following-sibling::div/form/div[2]/descendant::input"
    #window_course_name_result = tree.xpath("//div/following-sibling::div/form/div[2]/descendant::input")[0].value

    window_cousre_people = "xpath", "//input[@placeholder='请选择适应人群']"

    window_cousre_price = "xpath", "//input[@placeholder='请输入课程价格']"

    window_course_introduction = "xpath", "//textarea[@placeholder='请输入课程介绍']"

    window_course_sure = "xpath", "//span[text()='确 定']/parent::button"
    window_course_cancel = "xpath", "//span[text()='取 消']/parent::button"
    #查找下拉列表
    def ulli(self,name):
        name = name
        li = "xpath", "//body/div/div/div/ul/li/span[text()='{}']/parent::li".format(name)
        return li

    alert = "xpath","//div[@role='alert']/p"
    
    def search_course(self):
        self.clickbtn(self.course_model)
        self.send(self.course_name,'python语言')
        self.clickbtn(self.course_search)
        self.clickbtn(self.course_update_btn)
        self.clickbtn(self.window_course_introduction)
        time.sleep(2)
        course = {}
        course["course_subject_value"] = self.findelement(self.window_course_subject).get_attribute("value")
        course["cousre_name_value"] = self.findelement(self.window_course_name).get_attribute("value")
        course["cousre_people_value"] = self.findelement(self.window_cousre_people).get_attribute("value")
        course["cousre_price_value"] = self.findelement(self.window_cousre_price).get_attribute("value")
        course["introduction_value"] = self.findelement(self.window_course_introduction).get_attribute("value")
        self.clickbtn(self.window_course_cancel)
        #time.sleep(3)
        return course
    
    def add_course(self):
        self.clickbtn(self.course_model)
        self.clickbtn(self.course_add_button)
        self.clickbtn(self.window_course_subject)
        select = ()
        select = self.ulli('Python')
        print(select)
        time.sleep(1)
        self.clickbtn(select)
        self.send(self.window_course_name,'测试1001')
        self.clickbtn(self.window_cousre_people)
        time.sleep(1)
        select = self.ulli("小白学员")
        time.sleep(1)
        self.clickbtn(select)
        self.send(self.window_cousre_price,'1000')
        self.send(self.window_course_introduction,'测试用的')
        self.clickbtn(self.window_course_sure)
        time.sleep(1)
        text = self.gettext(self.alert)
        print("有没有值："+text)
        return text
        

if __name__ == '__main__':
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('http://kdtx-test.itheima.net/')
    LoginPage(driver).login_system()
    #CoursePage(driver).search_course()
    CoursePage(driver).add_course()
