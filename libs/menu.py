# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from elements import elements as els
from report import report
from forms import FormsFactory


class Menu(object):

    def __init__(self, page):
        self.page = page
        self.browser = page.browser

    @report.step('Click "start" menu')
    def click_start_menu(self):
        self.browser.click(els.menu_start)

    def _expand_to(self, menu_item):
        self.click_start_menu()

        def get_parents(item, items=[]):
            if item.parent:
                items.append(item.parent)
                get_parents(item.parent)
            else:
                return items

        for parent_item in reverse(get_parents(menu_item)):
            self.browser.click(parent_item)       

    def click(self, menu_item):
        with report.step('Click menu item "%s"' % menu_item):
            self._expand_to(menu_item)
            self.browser.click(menu_item)

        if menu_item.form:
            form = FormsFactory.get_form(menu_item.form, self.page)
            self.page.forms.append(form)
