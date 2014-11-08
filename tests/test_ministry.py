# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"


from report import report


def test_schools_list(ministry_page):
    """https://testlink.it.ru/education/school-323
    """

    ethalon_len = 7

    schools_form = ministry_page.menu.click(els.schools)
    schools = schools_form.items

    with report.step('Check that schools amount is %s.' % ethalon_len):
        assert_that(len(schools), equal_to(ethalon_len), 'Schools amount mismatches ethalon.')

def test_add_school(ministry_page, db):
    """https://testlink.it.ru/education/school-352
    """

    school_name = u'Школа с углубленным изучением иностранных языков'

    schools_form = ministry_page.menu.click(ministry_page.gui.schools_mnu)
    add_school_form = schools_form.click_add_btn()
    add_school_form.set_school(school_name)
    add_school_form.confirm()

    with report.step('Check that school "%s" is added' % school_name):
        assert_that(db.schools[-1].name, equal_to(school_name), 'School isn\'t added')