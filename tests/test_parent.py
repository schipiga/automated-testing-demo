# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

import pytest
from hamcrest import assert_that, equal_to, contains_string

from libs.marks import marks
from libs.report import report


@report.feature('e-school')
@report.story('parent')
@marks.full
@marks.sanity
def test_queue_information(parent_page):
    """https://testlink.it.ru/education/school-392
    """
    ethalon = 5

    queue_form = parent_page.menu.click(parent_page.gui.queue_mnu)
    queue_form.select_child(1)

    with report.step('Check that child queue is %s.'):
        assert_that(queue_form.info_text, equal_to(ethalon), 'Mismatched child queue.')


@report.feature('e-school')
@report.story('parent')
@marks.full
@marks.smoke
@pytest.mark.parametrize("child_name", (u'Маша', u'Алена', u'Витя'),
                         ids=(u'Маша', u'Алена', u'Витя'))
def test_child_scores(parent_page, child_name):
    """https://testlink.it.ru/education/school-592
    """
    scores_form = parent_page.menu.click(parent_page.gui.scores_mnu)
    scores_form.select_child(child_name)
    
    with report.step('Check that child has scores today'):
        assert_that(scores_form.scores, 'Oops! No scores')


@report.feature('e-school')
@report.story('parent')
@marks.full
@marks.accept
def test_parents_meeting_info(parent_page):
    """https://testlink.it.ru/education/school-615
    """
    meeting_time = '17:00'

    meetings_form = parent_page.menu.click(parent_page.gui.meetings_mnu)
    meetings_form.select_meeting()

    with report.step('Check that meeting will be at %s' % meeting_time):
        assert_that(meetings_form.info_label, contains_string(meeting_time), 'Meeting mismatched')
