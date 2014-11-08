# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from ..utils import to_snake_case


def register_form(cls):
    FormFactory.forms[to_snake_case(cls.__name__)] = cls
    return cls


class FormFactory(object):
    forms = {}

    @classmethod
    def get_form(self, name, page):
        return self.forms[name](page)