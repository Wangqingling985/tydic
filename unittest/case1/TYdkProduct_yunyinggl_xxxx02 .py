
import unittest
from selenium import webdriver
from time import sleep
# 导包
import time
import sys

from selenium.webdriver import ActionChains

'''1、系统页面访问、登录：点击登录按钮-输入账号密码-登录-退出'''



class TestLoginOut(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.url = 'http://10.142.101.156:9094'
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login1(self):
        driver = self.driver
        driver.find_element_by_id('username').send_keys('yanghy_dic')
        driver.find_element_by_id('password').send_keys('123456')
        driver.find_element_by_xpath('//*[@id="myform"]/fieldset/div[2]/button').click()
        # 获取登录信息
        # 获取登录信息
        login_info = driver.find_element_by_xpath('/html/body/div/div/div[1]/ul/li/div').text
        print('登录账号信息:',login_info)
        try:
            self.assertIn("杨会毅", login_info)
        except AssertionError:
            now_time = time.strftime('%Y-%m-%d %H_%M_%S')
            exc_info = sys.exc_info()
            # print(type(exc_info))
            # print(exc_info)
            print('登录失败！')
            driver.get_screenshot_as_file('../image/%s-%s.png' % (now_time, exc_info[1]))
            raise
        else:
            print('http://10.142.101.156:9094 登录成功！！！')


    # def test_login2(self):
    #     driver = self.driver
    #     driver.find_element_by_xpath('//*[@id="门户管理$Menu"]/li[1]/div').click()
    #     driver.find_element_by_xpath('//*[@id="服务管理$Menu"]/li[1]').click()
    #     sleep(3)
    #     driver.find_element_by_xpath('//*[@id="服务管理$Menu"]/li[12]').click()
    #     sleep(5)
    #     iframe=driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/iframe')
    #     driver.switch_to.frame(iframe)
    #     driver.find_element_by_xpath("//*[contains(text(),'全国调用总排行')]").click()
    #     sleep(2)
    #     driver.find_element_by_css_selector('[class="layui-layer-btn0"]').click()
    #     driver.switch_to.default_content()

    def test_logout(self):
        driver = self.driver
        ActionChains(driver).move_to_element(driver.find_element_by_xpath("//*[contains(text(),'杨会毅')]")).perform()
        sleep(3)
        driver.find_element_by_xpath("//*[contains(text(),'退出')]").click()
        print('退出登录')
        sleep(2)

if __name__ == '__main__':
    unittest.main()
