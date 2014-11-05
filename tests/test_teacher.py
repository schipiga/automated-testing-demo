# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"


def test_transfer_pupil_another_class(teacher_page):
    """https://testlink.it.ru/education/school-927
    """
    transfer_form = teacher_page.menu.click(Transfer)
    transfer_form.select_pupil()
    transfer_form.change_class()
    transfer_form.confirm()