# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from libs.report import report


def test_valid_authentication(browser, login_page):
    """https://testlink.it.ru/education/school-235
    """
    login_page.set_login('admin')
    login_page.set_password('admin')
    login_page.submit()
    user_page = browser.current_page
    auth_cookie = user_page.cookies.get('auth_key')

    with report.step('Check that auth_key is in cookies'):
        assert_that(auth_cookie)

    with report.step('Check that user_page is opened'):
        assert_that(user_page.title, equal_to(u'Личный кабинет'), 'Invalid page title')

def test_authentication_stored(browser, main_page):
    """https://testlink.it.ru/education/school-233
    """
    main_page.set_login('admin')
    main_page.set_password('admin')
    main_page.enable_remember_me()
    main_page.submit()
    browser.close()
    browser.launch()
    page = browser.open('/admin')

    with report.step('Check that session stored'):
        assert_that(page.title, equal_to(u'Личный кабинет'), 'Invalid page title')


def test_authentication_not_stored():
    """https://testlink.it.ru/education/school-234
    """
    main_page.set_login('admin')
    main_page.set_password('admin')
    main_page.submit()
    browser.close()
    browser.launch()
    page = browser.open('/')

    with report.step('Check that session is\'n stored'):
        assert_that(page.title, equal_to(u'Электронная школа: РФ'), 'Invalid page title')
