# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from selenium import webdriver

from fake_driver import FakeDriver as driver
from forms import FormFactory
from pages import PageFactory
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
        self._app_host = value

    @report.step('Launch browser')
    def launch(self):
        pass

    def open(self, path):
        url = self.app_host + path
        with report.step('Open url "%s"' % url):
            self.driver.get(url)
            self.wait_dom_build()
            return self.current_page

    def wait_dom_build(self):
        pass

    def right_click(self, gui_component):
        with report.step('Right click GUI "%s"' % gui_component.name):
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

        if getattr(gui_component, 'form', None):
            form = FormFactory.get_form(gui_component.form, self.current_page)
            self.current_page.forms.append(form)
            return form

    def wait_element(self, timeout=30):
        pass

    def set_text(self, gui_component, text):
        element = self.find_element(gui_component)
        element.set_text(text)

    def get_text(self, gui_component):
        element = setf.find_element(gui_component)
        return element.get_text()

    @property
    def driver(self):
        return self._driver

    @report.step('Close browser')
    def close(self):
        pass

    def enable(self, gui_component):
        pass

    def disable(self, gui_component):
        pass
