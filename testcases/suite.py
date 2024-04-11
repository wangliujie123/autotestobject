# _*_ coding:utf-8 _*_
import unittest
import HTMLTestRunner
import  time
import sys
sys.path.append("../page_object")
from common.function import project_path

if __name__ == '__main__':
    test_dir= project_path() + "/testcases"
    tests=unittest.defaultTestLoader.discover(test_dir,
                                                     pattern ='*_test.py',
                                                    top_level_dir=None)
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    filepath= project_path() + "/Reports/" + now + '.html'
    fp=open(filepath,'wb')
    #Define report title and description
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试报告',description=u'测试报告')
    runner.run(tests)
    fp.close()
