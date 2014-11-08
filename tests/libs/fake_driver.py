# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"


class FakeDriver(object):

    def __init__(self):
        self._url = None

    def get(self, url):
        self._url = url

    @property
    def current_url(self):
        return self._url

    def find_element(self):
        return FakeElement()


class FakeElement(object):

    def click(self):
        pass

    def set_text(self, text):
        pass

    def get_text(self):
        pass