import sys
sys.path.append("../page_object")
import time,pytest
from base.base import  Base
from selenium.webdriver.common.by import By
from selenium import webdriver
from pageobject.login_page import LoginPage




class CoursePage(Base):


#元素定位
    #课程管理菜单
    course_model = "xpath", "//a[@href='#/course']"
    #课程名称搜索框
    course_name = "xpath", "//input[@placeholder='请输入课程名称']"
    #搜索按钮
    course_search = "xpath", "//span[text()='搜索']/parent::button"
    #修改按钮
    course_update_btn = "xpath", "//span[text()='修改']/parent::button"
    #添加课程按钮
    course_add_button = "xpath", "//span[text()='添加课程']/parent::button"
    #课程详情页课程选择框
    window_course_subject = "xpath", "//div/following-sibling::div/form/descendant::input[@placeholder='请选择课程学科']"
    #
    window_course_name = "xpath", "//div/following-sibling::div/form/div[2]/descendant::input"
    #window_course_name_result = tree.xpath("//div/following-sibling::div/form/div[2]/descendant::input")[0].value

    window_cousre_people = "xpath", "//input[@placeholder='请选择适应人群']"

    window_cousre_price = "xpath", "//input[@placeholder='请输入课程价格']"

    window_course_introduction = "xpath", "//textarea[@placeholder='请输入课程介绍']"
    #详情页确定按钮
    window_course_sure = "xpath", "//span[text()='确 定']/parent::button"
    #详情页取消按钮
    window_course_cancel = "xpath", "//span[text()='取 消']/parent::button"
    #查找下拉列表
    def ulli(self,name):
        name = name
        li = "xpath", "//body/div/div/div/ul/li/span[text()='{}']/parent::li".format(name)
        return li

    alert = "xpath","//div[@role='alert']/p"

#查找课程
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
        if pytest.assume(course["course_subject_value"],"python"):
            print("查询成功")
        else:
            print("查询失败")
        print("执行完毕")
    

#添加课程
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
        try:
            assert "失败" in text
        except:
            print("失败了")
        print("继续吗")
        

if __name__ == '__main__':
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('http://kdtx-test.itheima.net/')
    LoginPage(driver).login_system()
    #CoursePage(driver).search_course()
    CoursePage(driver).add_course()
