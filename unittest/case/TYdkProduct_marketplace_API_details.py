
import unittest

import sys, time
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains

'''1、系统页面访问、登录：点击登录按钮-输入账号密码-登录
   2、点击应用开放（顶部）-用户当前位置-应用开放
   3、API详情：API调用页-API详情页-编码说明页-调用示例页-服务附件下载页-swagger下载页-SDK下载页'''

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

        # API详情:API调用
        driver.find_element_by_xpath('//*[@id="topServiceDiv"]/div[2]/div[2]/em').click()
        sleep(2)
        # API详情
        driver.find_element_by_xpath('//*[@id="subNav"]/a[2]/li').click()
        sleep(2)
        # 编码说明
        driver.find_element_by_xpath('//*[@id="subNav"]/a[3]/li').click()
        # 调用示例
        driver.find_element_by_xpath('//*[@id="subNav"]/a[4]/li').click()
        sleep(2)
        # 服务附件下载
        driver.find_element_by_xpath('//*[@id="subNav"]/a[5]/li').click()
        # swagger下载
        driver.find_element_by_xpath('//*[@id="subNav"]/a[6]/li').click()
        driver.find_element_by_xpath("//*[contains(text(),'用户终端识别.json')]").click()
        # SDK下载
        driver.find_element_by_xpath('//*[@id="subNav"]/a[7]/li').click()
        driver.find_element_by_link_text('sdk服务调用文档.doc').click()

        # 获取SDK下载页信息
        sdk_info = driver.find_element_by_xpath("//*[contains(text(),'sdk服务调用文档.doc')]").text
        print('SDK下载信息:', sdk_info)


        try:
            self.assertEqual("sdk服务调用文档.doc",sdk_info)
        except AssertionError:
            now_time = time.strftime('%Y-%m-%d %H_%M_%S')
            exc_info = sys.exc_info()
            # print(type(exc_info))
            # print(exc_info)
            print('API详情查询失败！')
            driver.get_screenshot_as_file('../image/%s-%s.png' % (now_time, exc_info[1]))
            raise
        else:
            print('API详情查询成功！！！')








    def tearDown(self):
        sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
