# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from selenium import webdriver

from fake_driver import FakeDriver as driver
from page import PageFactory
from report import report


class BrowserError(Exception):
    pass


class Browser(object):

    def __init__(self, browser_name):
        self._driver = driver()
        self._app_host = None

    @property
    def app_host(self):
        return self._app_host

    @app_host.setter
    def app_host(self, value):
        return self._app_host = value

    @report.step('Launch browser')
    def launch(self):
        pass

    def open(self, url):
        with report.step('Open url "%s"' % url):
            self._driver.get(url)
            self.wait_dom_build()
            return self.current_page

    def wait_dom_build(self):
        pass

    def right_click(self):
        pass

    def double_click(self):
        self.click()
        sleep(.5)
        self.click()

    @property
    def current_page(self):
        return PageFactory.get_page(self._driver.current_url, self)

    def find_element(self, gui_component):
        return self._driver.find_element(gui_component)

    def click(self, gui_component):
        element = self.find_element(gui_component)
        element.click()

    def wait_element(self, timeout=30):
        pass

    def set_text(self, gui_component, text):
        element = self.find_element(gui_component)
        element.set_text(text)

    def get_text(self, gui_component):
        element = setf.find_element(gui_component)
        return element.get_text()

    def driver(self):
        return self._driver

    @report.step('Close browser')
    def close(self):
        pass

    def enable(self, gui_component):
        pass

    def disable(self, gui_component):
        pass
