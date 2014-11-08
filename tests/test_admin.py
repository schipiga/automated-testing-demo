# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"


def test_add_statement_school(browser, admin_page, els, db):
    """https://testlink.it.ru/education/school-263
    """

    school_name = u"3-я специализированная школа"

    statements_form = admin_page.menu.click(admin_page.gui.statements_mnu)
    statement = statements_form.select_statement(1)
    browser.right_click(statement)
    transfer_form = browser.click(statements_form.gui.transfer_btn)
    transfer_form.choose_school(school_name)
    transfer_form.confirm()

    with report.step('Check that statement was forwarded to school %s' % school_name):
        assert_that(db.statements.first.school.name, equal_to(school_name), 'Invalid school')
