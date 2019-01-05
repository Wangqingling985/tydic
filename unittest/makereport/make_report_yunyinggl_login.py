
import unittest
import time
from tools.HTMLTestRunner import HTMLTestRunner
from tools.HTMLTestReportCN import HTMLTestRunner

if __name__=='__main__':
    case_dir='../case1/'
    discover=unittest.defaultTestLoader.discover(case_dir,pattern='TYdkProduct_*.py')
    report_dir='../report/'
    now_time=time.strftime('%Y%m%d %H%M%S')
    report_name=report_dir+now_time+' report.html'

    with open(report_name,'wb') as f:

        # 中文报告设置
        runner=HTMLTestRunner(stream=f,verbosity=2,title='天源迪科生产环境 基础能力系统项目测试报告',description='平台:Windows10,浏览器: Google Chrome 71.0.3578.80（正式版本）（32 位）', tester='test02QA')

        runner.run(discover)



