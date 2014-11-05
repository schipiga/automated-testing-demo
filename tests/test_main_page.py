# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

import allure

from libs import marks


@marks.smoke
@marks.full
def test_available_main_page(main_page):
    """https://testlink.it.ru/education/school-115
    """
    with allure_step('Check that main page is opened'):
        assert_that(main_page.title, equal_to(u'Электронная школа: РФ'), 'Invalid main page title')
