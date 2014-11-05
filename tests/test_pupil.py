# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"


def test_send_message_teacher(pupil_page):
    """https://testlink.it.ru/education/school-582
    """
    chat_form = pupil_page.menu.click(Chat)
    chat_form.select_teacher()
    chat_form.send_message(u'Я заболел и завтра не приду')