# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"


def test_add_statement_school(browser, admin_page, els, db):
    """https://testlink.it.ru/education/school-263
    """

    statements_form = admin_page.menu.click(els.statements)
    statement = statements_form.select_statement(1)
    browser.right_click(statement)
    transfer_form = browser.click(els.transfer)
    transfer_form.choose_school(7)
    transfer_form.confirm()

    assert_that(db.statement[1].school, equal_to(7))
