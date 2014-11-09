# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from base_form import BaseForm
from form_factory import register_form
from ..report import report


@register_form
class ChatForm(BaseForm):

    def select_teacher(self, teacher_name):
        with report.step('Select teacher "%s"' % teacher_name):
            pass

    def send_message(self, msg_text):
        with report.step('Send message "%s"' % msg_text):
            pass
