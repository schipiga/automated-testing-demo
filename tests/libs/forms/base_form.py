# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from ..gui import GUI


class BaseForm(object):

    def __init__(self, page):
        self.page = page
        self.browser = page.browser
        self.gui = GUI(self.__class__.__name__)
