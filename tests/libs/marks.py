# -*- coding: utf-8 -*-

author = "chipiga86@yandex.ru"

import pytest


class marks(object):
    smoke = pytest.mark.smoke
    full = pytest.mark.full