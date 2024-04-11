import pytest

if __name__ == '__main__':
    pytest.main([
        '--report=_report.html',
        '--title=边缘组件自动化验收报告',
        '--tester=测试员',
        '--desc=报告描述信息',
        '--template=1'])