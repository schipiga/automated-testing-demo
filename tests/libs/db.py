# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"


class DB(str):

    def __new__(cls):
        return super(DB, cls).__new__(cls, 'empty')

    def __getattr__(self, *args, **kwgs):
        return self

    __getitem__ = __getslice__ = __getattr__
