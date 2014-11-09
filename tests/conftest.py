# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

import pytest

from libs.db import DB
from libs.browser import Browser


@pytest.yield_fixture(scope="session")
def db():
    db = DB()
    db.begin_transation()

    yield db

    db.rollback_transaction()


@pytest.fixture(scope='session')
def browser(request):
    browser_name = request.config.inicfg.config.get('pytest', 'browser')
    return Browser(browser_name)


@pytest.fixture(scope='session')
def web_app(request, browser):
    app_host = request.config.inicfg.config.get('pytest', 'host')
    browser.launch()
    browser.app_host = app_host
    return browser.open('/')


@pytest.fixture
def login_page(web_app):
    return web_app


@pytest.fixture
def admin_page(browser, login_page):
    login_page.set_login('admin')
    login_page.set_password('admin')
    login_page.submit()
    return browser.current_page


@pytest.fixture
def ministry_page(browser, login_page):
    login_page.set_login('ministry')
    login_page.set_password('ministry')
    login_page.submit()
    return browser.current_page


@pytest.fixture
def parent_page(browser, login_page):
    login_page.set_login('parent')
    login_page.set_password('parent')
    login_page.submit()
    return browser.current_page


@pytest.fixture
def pupil_page(browser, login_page):
    login_page.set_login('pupil')
    login_page.set_password('pupil')
    login_page.submit()
    return browser.current_page


@pytest.fixture
def teacher_page(browser, login_page):
    login_page.set_login('teacher')
    login_page.set_password('teacher')
    login_page.submit()
    return browser.current_page
