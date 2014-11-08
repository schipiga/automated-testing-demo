# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from base_form import BaseForm
from form_factory import register_form
from ..report import report


@register_form
class TransferForm(BaseForm):

    def choose_school(self, school_name):
        with report.step('Choose school "%s"' % school_name):
            pass

    @report.step('Confirm statement transfer')
    def confirm(self):
        self.browser.click(self.gui.submit_btn)
