# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from base_form import BaseForm
from form_factory import register_form
from ..report import report


@register_form
class SchoolsForm(BaseForm):

    @property
    @report.step('Get all schools')
    def items(self):
        return ['Средняя школа №%s' % i for i in xrange(1, 8)]

    @report.step('Click "add school" button')
    def click_add_btn(self):
        return self.browser.click(self.gui.add_school_btn)
