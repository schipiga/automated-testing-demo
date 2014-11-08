# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"


class FakeDriver(object):

    def __init__(self):
        self._url = None
        self.cookies = {'auth_key': True}

    def get(self, url):
        self._url = url

    @property
    def current_url(self):
        return self._url

    def find_element(self, gui_element):
        return FakeElement()


class FakeElement(object):

    def __init__(self):
        self.type = self.name = 'undefined'

    def click(self):
        pass

    def set_text(self, text):
        pass

    def get_text(self):
        pass