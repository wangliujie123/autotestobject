import sys
sys.path.append("../page_object")
from common.log import FrameLog
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex

#对base代码进行优化、增加
class Base():
    def __init__(self,driver):
        self.driver = driver
        self.log =FrameLog().log()

    def findelement(self, locator):
        try:
            self.log.info("通过" + locator[0] + "定位,元素是" + locator[1])
            return WebDriverWait(self.driver, 20).until(ex.presence_of_element_located(locator))
        except:
            # 在页面上没有定位到相应的元素
            self.log.error("定位元素失败！")

    #输入封装
    def send(self,locator,value):
        self.findelement(locator).send_keys(value)
    #click封装
    def clickbtn(self,locator):
        self.findelement(locator).click()
   # 单星号参数代表此处接受任意多个非关键字参数
    def findele(self,*args):
        try:
            print(args)
            self.log.info("通过"+args[0]+"定位,元素是"+args[1])
            return  self.driver.find_element(*args)
        except:
            #在页面上没有定位到相应的元素。
            self.log.error("定位元素失败！")
    #对元素click
    def click(self,*args):
        self.findele(*args).click()
    #输入值
    def sendkey(self,*args,value):
        self.findele(*args).send_keys(value)
    #调用js方法
    def js(self,str):
        self.driver.execute_script(str)

    def url(self):
        return  self.driver.current_url

    # 后退
    def back(self):
        self.driver.back()
    #前进
    def forword(self):
        self.driver.forward()
    #退出
    def quit(self):
        self.driver.quit()
    
    #切换到iframe
    # 窗口最大化
    def maxwin(self):
        self.driver.maximize_window()

    # 全屏
    def fulwin(self):
        self.driver.fullscreen_window()

    # 最小化
    def minwin(self):
        self.driver.minimize_window()

    # 切换窗口,针对两个窗口进行切换
    def newtab(self):
        h = self.driver.window_handles
        self.driver.switch_to.window(h[-1])

    # 获取文本
    def gettext(self, locator):
        return self.findelement(locator).text

    # 下拉框,选择某一个元素
    def select(self, *args, num):
        se = self.findele(*args)
        Select(se).select_by_index(num)

    # alert文本
    def alert(self):
        return self.driver.switch_to.alert.text

    # 获取属性
    def getattr(self, *args, attr):
        return self.findele(*args).get_attribute(attr)

    # 鼠标右键
    def contextclick(self, *args):
        ActionChains(self.driver).context_click(self.findele(*args)).perform()

    # 鼠标左键
    def clickhold(self, *args):
        ActionChains(self.driver).click_and_hold(self.findele(*args)).perform()

    # 双击
    def doubleclick(self, *args):
        ActionChains(self.driver).double_click(self.findele(*args)).perform()

    # 悬停
    def movetoele(self, *args):
        ActionChains(self.driver).move_to_element(self.findele(*args)).perform()

    # 拖拉操作
    def drag(self, *args):
        sour = self.driver.find_element(By.CSS_SELECTOR, args[0])
        slide = self.driver.find_element(By.CSS_SELECTOR, args[1])
        ActionChains(self.driver).drag_and_drop_by_offset(sour, slide.size['width'],
                                                            -slide.size["height"]).perform()
            
if __name__ =='__main__':
    pass