import pytest
from selenium import webdriver
import sys
sys.path.append("../page_object")
from pageobject.login_page import LoginPage
from common.exceldata import read_excel
from common.function import config_url,project_path

# 全局设置driver方法1
driver = None


@pytest.fixture(scope='session')  # 以实现多个.py跨文件使用一个session来完成多个用例
def browser():
    global driver
    '''定义全局driver参数'''
    if driver is None:
        driver = webdriver.Edge()
        driver.maximize_window()

    driver.get(config_url())
    driver.implicitly_wait(10)
    print("正在启动浏览器:Edge")
    login = LoginPage(driver)
    data = read_excel(project_path()+"/data/testdata.xlsx",1)
    username = data[0][1]
    password = data[1][1]
    res = login.login_system(username,password)

    yield driver
    driver.close()
    return driver
