# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from base_page import BasePage
from page_factory import register_page


@register_page
class AdminPage(BasePage):
    path = '/admin'

    #TODO only for demo, remove in real
    @property
    def title(self):
        return 'Личный кабинет'
