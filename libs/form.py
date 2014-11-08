# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"


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


class AddSchoolForm(Form):

    def set_name(self, name):
        

    def confirm(self):


class TransferForm(Form):

    def choose_school(self, school_number):
        pass

    @report.step('Click "confirm" button')
    def confirm(self):
        self.browser.click(self.els.confirm)
