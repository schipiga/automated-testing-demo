# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from libs.report import report


def test_send_message_teacher(pupil_page):
    """https://testlink.it.ru/education/school-582
    """

    msg_text = u'Я заболел и завтра не приду'

    chat_form = pupil_page.menu.click(Chat)
    chat_form.select_teacher()
    chat_form.send_message(msg_text)

    with report.step('Checking that message is sent'):
        assert_that(db.messages.first.text, equal_to(msg_text), 'Message isn\'t sent')
