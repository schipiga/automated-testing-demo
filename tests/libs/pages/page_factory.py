# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from urlparse import urlparse


def register_page(cls):
    PageFactory.pages[cls.path] = cls
    return cls


class PageFactory(object):
    pages = {}

    @classmethod
    def get_page(cls, url, browser):
        parsed_url = urlparse(url)
        return cls.pages[parsed_url.path](browser)
