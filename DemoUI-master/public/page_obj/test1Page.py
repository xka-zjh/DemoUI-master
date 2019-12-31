# _*_ coding:utf-8 _*_
__author__ = 'zjh'

import os,sys
from time import sleep

import driver
from public.models.GetYaml import getyaml
from public.page_obj.base import Page
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

testData = getyaml(setting.TEST_Element_YAML + '/' + 'test1.yaml')
class test1(Page):
    """
    学信网登录测试
    """
    # 点击登录按钮
    # dig_login_button_loc = (By.XPATH, testData.get_elementinfo(0))
    # # 选择账号密码登录
    # login_logintype_loc = (By.ID, testData.get_elementinfo(0))
    def dig_login(self):
        """
        百度登录
        :return:
        """
        # self.find_element(*self.dig_login_button_loc).click()
        # sleep(1)
        # self.find_element(*self.login_logintype_loc).click()
        # sleep(1)
    # 定位器，通过元素属性定位元素对象
    # 手机号输入框
    login_phone_loc = (By.ID, testData.get_elementinfo(0))
    # 密码输入框
    login_password_loc = (By.ID, testData.get_elementinfo(1))
    # 取消自动登录
    # keeplogin_button_loc = (By.XPATH, testData.get_elementinfo(4))
    # 单击登录
    login_user_loc = (By.XPATH, testData.get_elementinfo(2))
    # 退出登录
    # login_exit_loc = (By.ID, testData.get_elementinfo(3))
    # # 选择退出
    login_exit_button_loc = (By.XPATH, testData.get_elementinfo(3))
    login_exit_alert = (By.XPATH, testData.get_elementinfo(4))
    def login_phone(self, phone):
        """
        登录账号
        :param username:
        :return:
        """
        # sleep(1)
        self.find_element(*self.login_phone_loc).send_keys(phone)
    def login_password(self, password):
        """
        登录密码
        :param password:
        :return:
        """
        # sleep(1)
        self.find_element(*self.login_password_loc).send_keys(password)
    # def keeplogin(self):
    #     """
    #     取消单选自动登录
    #     :return:
    #     """
    #     self.find_element(*self.keeplogin_button_loc).click()
    def login_button(self):
        """
        登录按钮
        :return:
        """
        # sleep(1)
        self.find_element(*self.login_user_loc).click()
    def login_exit(self):
        """
        退出系统
        :return:
        """
        # above = self.find_element(*self.login_exit_loc)
        # ActionChains(self.driver).move_to_element(above).perform()
        # sleep(1)
        self.find_element(*self.login_exit_button_loc).click()
        sleep(1)
        self.find_element(*self.login_exit_alert).click()

    def user_login(self, phone, password):
        """
        登录入口
        :param username: 用户名
        :param password: 密码
        :return:
        """
        self.open()
        # self.dig_login()
        self.login_phone(phone)
        self.login_password(password)
        # sleep(1)
        # self.keeplogin()
        # sleep(1)
        self.login_button()
        # sleep(1)

    user_login_success_loc = (By.XPATH, testData.get_CheckElementinfo(0))
    exit_login_success_loc = (By.XPATH, testData.get_CheckElementinfo(1))
    phone_pawd_error1_hint_loc = (By.ID, testData.get_CheckElementinfo(2))
    phone_pawd_error2_hint_loc = (By.ID, testData.get_CheckElementinfo(3))
    # 登录成功用户名
    def user_login_success_hint(self):
        b = self.find_element(*self.user_login_success_loc).text
        return int(b)
    # 退出登录
    def exit_login_success_hint(self):
        return self.find_element(*self.exit_login_success_loc).text
    # 手机号或密码错误提示(1)
    def phone_pawd_error1_hint(self):
        return self.find_element(*self.phone_pawd_error1_hint_loc).text
    # 手机号或密码错误提示(2)
    def phone_pawd_erro2r_hint(self):
        return self.find_element(*self.phone_pawd_error2_hint_loc).text
    # 手机号或密码任何一项为空(提取文字)
    def phone_pawd_empty_hint(self):
        a = self.switch_alert_accept().text
        return a
    # 手机号或密码任何一项为空(确认弹窗)
    def phone_pawd_empty_hint_accept(self):
        self.switch_alert_accept().accept()