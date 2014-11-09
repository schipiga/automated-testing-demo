# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from base_page import BasePage
from page_factory import register_page


@register_page
class PupilPage(BasePage):
    path = '/pupil'
