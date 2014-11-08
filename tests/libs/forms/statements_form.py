# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from base_form import BaseForm
from form_factory import register_form
from ..report import report
from ..fake_driver import FakeElement as Element

@register_form
class StatementsForm(BaseForm):

    def select_statement(self, statement_number):
        with report.step('Select statement №%s' % statement_number):
            return Element()
