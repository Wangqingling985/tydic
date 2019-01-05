
import unittest

import sys, time
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

'''1、系统页面访问、登录：点击登录按钮-输入账号密码-登录
   2、点击应用开放（顶部）-用户当前位置-应用开放-浏览首页菜单
   3、API订阅页面:点击订阅按钮-输入或选择弹出选项-退出
'''

class TestLoginOut(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'http://10.142.101.156:9095'
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)


    def test_login(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/ul[2]/ul/li[1]/span').click()
        driver.find_element_by_id('username').send_keys('wangqingling')
        driver.find_element_by_id('password').send_keys('123456A!')
        driver.find_element_by_xpath('//*[@id="myform"]/fieldset/div[2]/button').click()
        sleep(2)
        # 点击基础能力系统(首页顶部）
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/ul[2]/li[2]/span/ul/li/div').click()
        driver.find_element_by_xpath('//*[@id="item_0$Menu"]/li[2]').click()
        sleep(5)

        '''点击应用开放（顶部）-用户当前位置-应用开放'''

        # 鼠标悬停
        action = ActionChains(driver)
        button = driver.find_element_by_xpath("//*[contains(text(),'应用开放')]")
        sleep(3)
        move_to_action = action.move_to_element(button)
        move_to_action.perform()
        # ActionChains(driver).move_to_element(driver.find_element_by_css_selector('button')).perform()
        sleep(2)
        driver.find_element_by_xpath("//*[contains(text(),'用户当前位置')]").click()
        sleep(2)
        # 应用开放
        driver.find_element_by_xpath('//*[@id="listTableDataDiv1"]/div/div[1]/a[1]').click()

        '''API订阅页面:点击订阅按钮-输入或选择弹出选项'''
        # API详情
        driver.find_element_by_xpath('//*[@id="topServiceDiv"]/div[3]/div[2]/em').click()
        # 订阅:填信息
        driver.find_element_by_css_selector('[class="but3 mgT10 po fr"]').click()
        driver.find_element_by_css_selector('[id="appName"]').send_keys('用户终端轨迹查询')

        driver.find_element_by_xpath('//*[@id="orderForm"]/table/tbody/tr[3]/td[2]/input[2]').click()
        # 下拉框（申请频率）
        sel = driver.find_element_by_id('frequence')
        sleep(2)
        Select(sel).select_by_index(2)
        # 调用总次数
        driver.find_element_by_xpath('//*[@id="orderForm"]/table/tbody/tr[4]/td[2]/input[2]').click()
        driver.find_element_by_css_selector('[id="totalTime"]').send_keys('20')
        # 适用范围
        driver.find_element_by_css_selector('[id="placeControlVal"]').click()
        driver.find_element_by_css_selector('[data-name="湖北"]').click()
        sleep(1)
        driver.find_element_by_css_selector('[class="aui-btn aui-btn-primary"]').click()

        # 下拉框（调用单位）
        sel = driver.find_element_by_id("unitId")
        # sleep(2)
        Select(sel).select_by_index(5)

        # 下拉框(调用平台）
        sel = driver.find_element_by_id("terraceId")
        # sleep(2)
        Select(sel).select_by_index(3)
        sleep(2)
        # 调用IP
        driver.find_element_by_css_selector('[name="ips"]').send_keys('192.168.129.116')
        driver.find_element_by_css_selector('[name="remark"]').send_keys('用户终端轨迹查询')
        sleep(2)

        # 获取订阅服务 页信息
        api_subscribe = driver.find_element_by_css_selector('[class="qrdy but2 fl mgL10"]').text
        print('点击订阅按钮弹出选项("提交"需要审批，暂不可选)：', api_subscribe)



        try:
            self.assertEqual("返回",api_subscribe)
        except AssertionError:
            now_time = time.strftime('%Y-%m-%d %H_%M_%S')
            exc_info = sys.exc_info()
            # print(type(exc_info))
            # print(exc_info)
            print('API订阅查询失败！')
            driver.get_screenshot_as_file('../image/%s-%s.png' % (now_time, exc_info[1]))
            raise
        else:
            print('API订阅查询成功！！！')




    def tearDown(self):
        sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
