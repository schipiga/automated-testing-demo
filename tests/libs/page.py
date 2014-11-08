# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

# from elements import elements as els
from menu import Menu
from report import report


def register_page(cls):
    PageFactory.pages[cls.url] = cls
    return cls


class PageFactory(object):
    pages = {}

    @classmethod
    def get_page(cls, url, browser):
        return cls.pages[url](browser)


class Page(object):

    url = None

    def __init__(self, browser):
        self.browser = browser
        self.menu = Menu(self)

    @property
    def title(self):
        return self.browser.current_title

    # @property
    # def url(self):
    #     return self.browser.current_url

@register_page
class LoginPage(Page):

    url = '/'

    def set_login(self, login):
        with report.step('Enter login "%s"' % login):
            self.browser.set_text(els.login, login)

    def set_password(self, password):
        with report.step('Enter password "%s"' % password):
            self.browser.set_text(els.password, password)

    @report.step('Enable "remember me"')
    def enable_remember_me(self):
        self.browser.enable(els.remember_me)

    @report.step('Disable "remember me"')
    def disable_remember_me(self):
        self.browser.disable(els.remember_me)

    @report.step('Click "submit" button')
    def submit(self):
        self.browser.click(els.submit)

    @property
    def title(self):
        return u'Электронная школа: РФ'
