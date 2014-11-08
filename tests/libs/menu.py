# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from report import report


class Menu(object):

    def __init__(self, page):
        self.page = page
        self.browser = page.browser

    @report.step('Click "start" menu')
    def click_start_menu(self):
        self.browser.click(self.page.gui.menu_start)

    def _expand_to(self, menu_item):
        self.click_start_menu()

        def get_parents(item, items=[]):
            if getattr(item, 'parent', None):
                items.append(item.parent)
                get_parents(item.parent)
            else:
                return items

        for parent_item in reversed(get_parents(menu_item)):
            self.browser.click(parent_item)       

    def right_click(self, menu_item):
        with report.step('Right click menu item "%s"' % menu_item):
            self._expand_to(menu_item)
            self.browser.right_click(menu_item)

    def click(self, menu_item):
        with report.step('Click menu item "%s"' % menu_item):
            self._expand_to(menu_item)
            return self.browser.click(menu_item)
