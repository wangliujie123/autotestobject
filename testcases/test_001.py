import sys
sys.path.append("../page_object")
import pytest
#import time,unittest,HTMLTestRunner
from common.function import project_path
from common.function import config_url
from pageobject.course_page import CoursePage


#单元测试
# class login_test(unittest.TestCase):
#     def setup_class(cls):
#         #cls.data = read_excel(project_path() + "/Data/testdata.xlsx", 0)
#         cls.driver = webdriver.Edge()
#         cls.driver.get(config_url())
#         cls.driver.maximize_window()
#         login = LoginPage(cls.driver)
#         res = login.login_system()

#     @pytest.mark.run(order=2)
#     def test_01(self):
#         course = CoursePage(self.driver)
#         res = course.search_course()
#         if pytest.assume(res["course_subject_value"],"python"):
#             print("查询成功")
#         else:
#             print("查询失败")

    
#     @pytest.mark.run(order=1)
#     def test_02(self):
#         course = CoursePage(self.driver)
#         res = course.add_course()
#         self.assertIn("失败",res)

#     def teardown_class(cls):
#         cls.driver.close()

# if __name__ == '__main__':
#     suiteTest = unittest.TestSuite()
#     suiteTest.addTest(test_one("test_01"))
#     filepath = project_path() + "/Reports/report.html"
#     fp = open(filepath, 'wb')
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='自动化测试报告', description="测试报告")
#     runner.run(suiteTest)
#     fp.close()


#查找课程
@pytest.mark.run(order=2)
def test_01(browser):
    course = CoursePage(browser)
    course.search_course()

    
#添加课程    
@pytest.mark.run(order=1)
def test_02(browser):
    course = CoursePage(browser)
    course.add_course()



