# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from base_form import BaseForm
from form_factory import register_form
from ..report import report


@register_form
class ScoresForm(BaseForm):

    def select_child(self, child_name):
        with report.step('Select child "%s"' % child_name):
            pass

    @property
    def scores(self):
        return (3, 5, 4, 5, 5)
