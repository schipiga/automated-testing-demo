# -*- coding: utf-8 -*-

author = "chipiga86@yandex.ru"


def to_snake_case(string):
    return ''.join(i if i == i.lower() else "_%s" % i.lower() for i in string)
