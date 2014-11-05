# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"


class Page(object):

    def __init__(self, tab, url):
        self.tab = tab
        self.browser = tab.browser
        self.url = url


class MainPage(Page):

    def set_login(self, login):
        pass

    def set_password(self, password):
        pass

    def remember_me(self):
        pass

    def submit(self):
        pass