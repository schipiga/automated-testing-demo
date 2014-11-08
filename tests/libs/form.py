# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from report import report
from utils import to_snake_case


def register_form(cls):
    FormFactory.forms[to_snake_case(cls.__name__)] = cls
    return cls


class FormFactory(object):
    forms = {}

    @classmethod
    def get_form(self, name, page):
        return forms[name](page)


class Form(object):

    def __init__(self, page):
        self.page = page
        self.browser = page.browser


@register_form
class StatementsForm(object):

    def select_statement(self, statement_number):
        return Element(statement_number)


class SchoolsForm(Form):

    def click_add(self):
        pass


class AddSchoolForm(Form):

    def set_name(self, name):
        pass        

    def confirm(self):
        pass


class TransferForm(Form):

    def choose_school(self, school_number):
        pass

    @report.step('Click "confirm" button')
    def confirm(self):
        self.browser.click(self.els.confirm)


class TransferForm(Form):

    def select_pupil(self, pupil_name):
        pass

    def select_grade(self, grade_name):
        pass
