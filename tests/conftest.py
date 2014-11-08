# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

import pytest
from libs.browser import Browser

# from ui import ui as UI

# @pytest.fixture(scope="session")
# def db():
# 	return DB()


# @pytest.yield_fixture(autouse=True)
# def prepare_db(db):
# 	db.begin_transation()

# 	yield

# 	db.rollback_transaction()

@pytest.fixture(scope='session')
def browser(request):
    browser_name = request.config.inicfg.config.get('pytest', 'browser')
    return Browser(browser_name)


@pytest.fixture(scope='session')
def web_app(request, browser):
    app_host = request.config.inicfg.config.get('pytest', 'host')
    browser.launch()
    browser.app_host = app_host
    return browser.open_page('/')


@pytest.fixture
def login_page(web_app):
    return web_app


# @pytest_fixture
# def admin_page(login_page):
#     login_page.set_login('admin')
#     login_page.set_password('admin')
#     login_page.submit()
#     return browser.current_page


# @pytest_fixture(scope='session')
# def ui():
#     return UI


# @pytest.fixture
# def teacher_page(login_page):
#     login_page.set_login('teacher')
#     login_page.set_password('teacher')
#     login_page.submit()
#     return browser.current_page
