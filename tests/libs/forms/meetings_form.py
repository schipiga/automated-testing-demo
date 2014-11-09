# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from base_form import BaseForm
from form_factory import register_form
from ..report import report


@register_form
class MeetingsForm(BaseForm):

    @report.step('Select meeting')
    def select_meeting(self):
        pass

    @property
    def info_label(self):
        return 'Next meeting will be 17.10.2015 at 17:00'
