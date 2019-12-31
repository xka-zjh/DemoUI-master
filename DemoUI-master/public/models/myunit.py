#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'zjh'

import unittest

from public.models.driver import browser


class MyTest(unittest.TestCase):
    """
    自定义MyTest类
    """
    #开启浏览器
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    #关闭浏览器
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()