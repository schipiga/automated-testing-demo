# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from hamcrest import assert_that, equal_to

from libs.marks import marks
from libs.report import report


@report.feature('e-school')
@report.story('admin')
@marks.sanity
@marks.full
def test_add_statement_school(browser, admin_page, db):
    """https://testlink.it.ru/education/school-263
    """

    school_name = "3-я специализированная школа"

    statements_form = admin_page.menu.click(admin_page.gui.statements_mnu)
    statement = statements_form.select_statement(1)
    browser.right_click(statement)
    transfer_form = browser.click(statements_form.gui.transfer_mnu)
    transfer_form.choose_school(school_name)
    transfer_form.confirm()

    with report.step('Check that statement was forwarded to school %s' % school_name):
        assert_that(db.statements.first.school.name, equal_to(school_name), 'Invalid school')
