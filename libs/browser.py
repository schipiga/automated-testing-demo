# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from selenium import webdriver


class BrowserError(Exception):
    pass


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

    @property
    def current_tab(self):
        return tab

    @property
    def current_page(self):
        return Page.get_page_by(self._driver.current_url, self.current_tab)
