# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from libs.report import report
from libs.marks import marks


@marks.full
@marks.accept
def test_transfer_pupil_another_class(teacher_page):
    """https://testlink.it.ru/education/school-927
    """

    pupil_name = u'Алексеев Олег Игоревич'
    grade_name = u'7B'

    with report.step(u'Check that %s is transfered to %s' % (pupil_name, grade_name)):
        pass
