# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from hamcrest import assert_that, equal_to

from libs.marks import marks
from libs.report import report


@report.feature('e-school')
@report.story('pupil')
@marks.full
@marks.smoke
def test_send_message_teacher(pupil_page, db):
    """https://testlink.it.ru/education/school-582
    """

    msg_text = 'Я заболел и завтра не приду'

    chat_form = pupil_page.menu.click(pupil_page.gui.chat_mnu)
    chat_form.select_teacher('Заболоцкий Илья Сергеевич')
    chat_form.send_message(msg_text)

    with report.step('Checking that message is sent'):
        assert_that(db.messages.first.text, equal_to(msg_text), 'Message isn\'t sent')
