# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from ..gui import GUI
from ..menu import Menu


class BasePage(object):

    path = None

    def __init__(self, browser):
        self.browser = browser
        self.forms = []
        self.menu = Menu(self)
        self.gui = GUI(self.__class__.__name__)

    @property
    def title(self):
        return self.browser.driver.current_title

    @property
    def cookies(self):
        return self.browser.driver.cookies

    @property
    def url(self):
        return self.browser.driver.current_url
