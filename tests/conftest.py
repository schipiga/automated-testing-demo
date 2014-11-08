# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

import pytest

from elements import elements
import config

@pytest.fixture(scope="session")
def db():
	return DB()


@pytest.yield_fixture(autouse=True)
def prepare_db(db):
	db.begin_transation()

	yield

	db.rollback_transaction()

@pytest.fixture(scope='session')
def browser():
    return Browser()


@pytest.fixture
def web_app(browser):
    return browser.open_page(config.app_host)


@pytest_fixture
def login_page(web_app):
    return web_app


@pytest_fixture
def admin_page(login_page):
    login_page.set_login('admin')
    login_page.set_password('admin')
    login_page.submit()
    return browser.current_page

@pytest_fixture(scope='session')
def els():
    return elements
