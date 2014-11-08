# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from base_form import BaseForm
from form_factory import register_form
from ..report import report


@register_form
class AddSchoolForm(BaseForm):

    def set_school(self, school_name):
        with report.step('Set school name "%s"' % school_name):
            pass

    @report.step('Click button to confirm school addition')
    def confirm(self):
        return self.browser.click(self.gui.submit)
