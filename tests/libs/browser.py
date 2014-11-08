# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from selenium import webdriver

from page import PageFactory
from report import report


class BrowserError(Exception):
    pass


class Browser(object):

    def __init__(self, browser_name):
        # driver = getattr(webdriver, browser_name)
        # self._driver = driver()
        # self.tabs = []
        self.app_host = None

    @report.step('Launch browser')
    def launch(self):
        pass

    def open_page(self, url):
        # self._driver.get('/')
        self.wait_dom_build()
        return self.current_page

    def wait_dom_build(self):
        pass

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
        # url = self._driver.current_url
        url = '/'
        return PageFactory.get_page(url, self)

    @property
    def current_title(self):
        return self._driver.title

    @property
    def current_url(self):
        return self._driver.url

    def find_element(self, gui_component):
        pass

    def click(self, gui_component):
        element = self.find_element(gui_component)
        # element.click()

    def wait_element(self):
        self.find_element

    def set_text(self, gui_component, value):
        pass
