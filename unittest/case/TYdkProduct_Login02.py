
import unittest
from selenium import webdriver
from time import sleep
# 导包
import time
import sys

from selenium.webdriver import ActionChains

'''2、进入项目：点击工作台-我的产品-点击任意产品（点击即席查询）-跳转至开发工具'''

class TestLoginOut(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = 'http://10.142.101.156:9095'
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        print('当前页面地址为:', self.driver.current_url)
        print('当前页面标题为:', self.driver.title)

    def test_login(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/ul[2]/ul/li[1]/span').click()
        driver.find_element_by_id('username').send_keys('wangqingling')
        driver.find_element_by_id('password').send_keys('123456A!')
        driver.find_element_by_xpath('//*[@id="myform"]/fieldset/div[2]/button').click()

        # 点击基础能力系统(首页顶部）
        driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/ul[2]/li[2]/span/ul/li/div').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="item_0$Menu"]/li[2]').click()


        current_handle = driver.current_window_handle
        print('当前窗口的句柄为:', current_handle)
        # 点击工作台
        driver.find_element_by_xpath("//*[contains(text(),'工作台')]").click()
        sleep(2)
        '''点击即席查询-->进入我的产品'''
        driver.find_element_by_xpath(
            '/html/body/div/div/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div/div/div[3]').click()
        handles = driver.window_handles
        print('所有窗口的句柄为:', handles)
        driver.switch_to_window(handles[2])

        # 获取产品信息
        kf_info = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/ul/li[1]').text

        # 总菜单
        # eles = driver.find_elements_by_xpath('/html/body/div/div[2]/div[1]/div/ul')
        # for ele in eles:
        #     print(ele.text)


        print('我的产品信息:',kf_info)
        try:
            self.assertIn("开发工具",kf_info)
        except AssertionError:
            now_time = time.strftime('%Y-%m-%d %H_%M_%S')
            exc_info = sys.exc_info()
            # print(type(exc_info))
            # print(exc_info)
            print('进入项目失败！！')
            driver.get_screenshot_as_file('../image/%s-%s.png' % (now_time, exc_info[1]))
            raise
        else:
            print('跳转至开发工具,进入项目成功！！！')

    def tearDown(self):
        sleep(3)
        # self.driver.quit()

if __name__ == '__main__':
    unittest.main()
