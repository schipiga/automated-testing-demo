# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from base_page import BasePage
from page_factory import register_page
from ..report import report


@register_page
class LoginPage(BasePage):

    path = '/'

    def set_login(self, login):

        #TODO only for demo, remve in real
        self.username = login

        with report.step('Enter login "%s"' % login):
            self.browser.set_text(self.gui.login, login)

    def set_password(self, password):
        with report.step('Enter password "%s"' % password):
            self.browser.set_text(self.gui.password, password)

    @report.step('Enable "remember me"')
    def enable_remember_me(self):
        self.browser.enable(self.gui.remember_me)

    @report.step('Disable "remember me"')
    def disable_remember_me(self):
        self.browser.disable(self.gui.remember_me)

    @report.step('Click "login" button')
    def submit(self):
        self.browser.click(self.gui.submit)

        # TODO only for demo. remove in real
        self.browser._driver._url = '/%s' % self.username

    #TODO only for demo, remove in real
    @property
    def title(self):
        return 'Электронная школа: РФ'
