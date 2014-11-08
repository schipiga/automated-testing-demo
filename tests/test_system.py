# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from libs.report import report

def test_transfer_successful_pupils():
    """https://testlink.it.ru/education/school-829
    """
    with report.step('Check that all pupils are trunsfered'):
        pass
    

def test_stupid_pupils_same_grade():
    """https://testlink.it.ru/education/school-476
    """
    with report.step('Check that stupid pupils stay at the same grade'):
        pass
