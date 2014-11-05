# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"


def test_add_statement_school(admin_page):
    """https://testlink.it.ru/education/school-263
    """

    statements_form = admin_page.menu.click(Statements)
    statement = statements_form.select_statement(1)
    statement.right_click()
    transfer_form = statement.click(Transfer)
    transfer_form.click_separate()
    transfer_form.confirm()