
import unittest
from selenium import webdriver
from time import sleep
# 导包
import time
import sys

from selenium.webdriver import ActionChains

'''1、系统页面访问、登录：点击登录按钮-输入账号密码-登录-退出'''

class TestLoginOut1(unittest.TestCase):
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

        # 获取登录信息
        login_info = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/ul[2]/ul/li/div/div/span[2]').text
        # login_info = driver.find_element_by_xpath(
        #     '/html/body/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/h3').text
        print('登录账号信息:',login_info)
        try:
            self.assertIn("王庆玲", login_info)
            # self.assert login_info == "甜橙白条标签评分"
        except AssertionError:
            now_time = time.strftime('%Y-%m-%d %H_%M_%S')
            exc_info = sys.exc_info()
            # print(type(exc_info))
            # print(exc_info)
            print('登录失败！')
            driver.get_screenshot_as_file('../image/%s-%s.png' % (now_time, exc_info[1]))
            raise
        else:
            print('登录成功！！！')

        ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[contains(text(),'王庆玲')]")).perform()
        sleep(3)
        driver.find_element_by_xpath("//*[contains(text(),'退出')]").click()

    def tearDown(self):
        sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
