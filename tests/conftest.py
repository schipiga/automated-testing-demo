# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

import pytest

import config

@pytest.fixture(scope="session")
def db():
	return DB()


@pytest.yield_fixture(autouse=True)
def prepare_db(db):
	db.begin_transation()

	yield

	db.rollback_transaction()


@pytest.fixture
def web_app(browser):
    browser.launch()
    page = browser.open_page(config.app_host)
    return page


@pytest_fixture
def main_page(web_app):
    return web_app