# -*- coding: utf-8 -*-

author = "chipiga86@yandex.ru"


def to_snake_case(string):
    return ''.join(i if i == i.lower() else "%s%s" % ('_' * bool(j), i.lower()) for j, i in enumerate(string))
