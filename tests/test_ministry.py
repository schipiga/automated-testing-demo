# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"


from report import report


def test_schools_list(ministry_page):
    """https://testlink.it.ru/education/school-323
    """
    schools_form = ministry_page.menu.click(els.schools)
    schools = schools_form.items
    with report.step('Check schools amount is %s.' % ethalon_len):
        assert_that(schools_len, equal_to(ethalon_len), 'Schools amount mismatches ethalon.')

def test_add_school(ministry_page, db):
    """https://testlink.it.ru/education/school-352
    """
    schools_form = ministry_page.menu.click(Schools)
    add_school_form = schools_form.click_add()
    add_school_form.set_name('')
    add_school_form.confirm()

    assert_that(db.schools[-1].name, equal_to(''))