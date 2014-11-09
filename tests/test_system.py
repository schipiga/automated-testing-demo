# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from libs.marks import marks
from libs.report import report


@report.feature('e-school')
@report.story('system')
@marks.full
@marks.accept
def test_transfer_successful_pupils():
    """https://testlink.it.ru/education/school-829
    """
    with report.step('Check that all pupils are trunsfered'):
        pass
    

@report.feature('e-school')
@report.story('system')
@marks.full
@marks.sanity
def test_stupid_pupils_same_grade():
    """https://testlink.it.ru/education/school-476
    """
    with report.step('Check that stupid pupils stay at the same grade'):
        pass
