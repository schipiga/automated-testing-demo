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

    error_messages = []
    if not user_page.title == u'Личный кабинет':
        error_messages.append('Invalid user page title.')
    if not auth_cookie:
        error_messages.append('No auth cookie.')

    with report.step('Check that no problem after authentication.'):
        assert_that(not error_messages, 'There are some errors.\n%s', '\n'.join(error_messages))


def test_authentication_stored(browser, main_page):
    """https://testlink.it.ru/education/school-233
    """
    main_page.set_login('admin')
    main_page.set_password('admin')
    main_page.enable_remember_me()
    main_page.submit()
    browser.close()
    browser.launch()
    page = browser.open_app()


def test_authentication_not_stored():
    """https://testlink.it.ru/education/school-234
    """
    main_page.set_login('admin')
    main_page.set_password('admin')
    main_page.submit()
    browser.close()
    browser.launch()
    page = browser.open_app()
