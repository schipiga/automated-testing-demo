# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from selenium import webdriver


class Browser(object):

    def __init__(self, browser_name):
        driver = getattr(webdriver, browser_name)
        self._driver = driver()
        self.tabs = []

    def click(self):
        pass

    def right_click(self):
        pass

    def double_click(self):
        self.click()
        sleep(.5)
        self.click()

    def new_tab(self, url):
        pass    
