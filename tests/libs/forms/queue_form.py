# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from base_form import BaseForm
from form_factory import register_form
from ..report import report


@register_form
class QueueForm(BaseForm):

    def select_child(self, child_number):
        with report.step('Select child №%s' % child_number):
            pass

    @property
    def info_text(self):
        return 5
