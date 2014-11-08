# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"


class Tab(object):

    def __init__(self, browser):
        self.browser = browser
        self.page = Page(self)