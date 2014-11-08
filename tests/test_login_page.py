# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from hamcrest import assert_that, equal_to

from libs.report import report
from libs.marks import marks


@marks.smoke
@marks.full
def test_available_login_page(login_page):
    """https://testlink.it.ru/education/school-115
    """
    with report.step('Check login main page is opened'):
        assert_that(login_page.title, equal_to(u'Электронная школа: РФ'), 'Invalid login page title')
