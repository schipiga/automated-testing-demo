# -*- coding: utf-8 -*-

author = "chipiga86@yandex.ru"

import pytest


class marks(object):
    accept = pytest.mark.accept
    full = pytest.mark.full
    sanity = pytest.mark.sanity
    smoke = pytest.mark.smoke
