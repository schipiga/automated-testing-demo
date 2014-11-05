# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"


def test_valid_authentication():
    """https://testlink.it.ru/education/school-235
    """
    main_page.set_login('admin')
    main_page.set_password('admin')
    user_page = main_page.submit()
    auth_cookie = user_page.cookies.get('auth_key')

    error_messages = []
    if not user_page.title == u'Личный кабинет':
        error_messages.append('Invalid user page title.')
    if not auth_cookie:
        error_messages.append('No auth cookie.')

    with allure.step('Check that no problem after authentication.'):
        assert_that(not error_messages, 'There are some errors.\n%s', '\n'.join(error_messages))


def test_authentication_stored(main_page):
    """https://testlink.it.ru/education/school-233
    """
    main_page.set_login('admin')
    main_page.set_password('admin')
    main_page.remember_me()
    user_page = main_page.submit()
    browser.close()
    browser.launch()
    page = browser.open_app()


def test_authentication_not_stored():
    """https://testlink.it.ru/education/school-234
    """
    main_page.set_login('admin')
    main_page.set_password('admin')
    user_page = main_page.submit()
    browser.close()
    browser.launch()
    page = browser.open_app()
