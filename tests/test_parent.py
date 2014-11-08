# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from hamcrest import assert_that, equal_to, contains

from libs.marks import marks
from libs.report import report


@marks.full
@marks.sanity
def test_queue_information(parent_page):
    """https://testlink.it.ru/education/school-392
    """
    ethalon = 5

    queue_form = parent_page.menu.click(Queue)
    queue_form.select_child(1)

    with report.step('Check that child queue is %s.'):
        assert_that(queue_form.info_text, equal_to(ethalon), 'Mismatched child queue.')


@marks.full
@marks.smoke
@pytest.fixture.parametrize(child_name=(u'Маша', u'Алена', u'Витя'))
def test_child_scores(parent_page, child_name):
    """https://testlink.it.ru/education/school-592
    """
    scores_form = parent_page.menu.click(Scores)
    scores_form.select_child(child_id)
    
    with report.step('Check that child has scores today'):
        assert_that(scores_form.scores, 'Oops! No scores')


@marks.full
@marks.accept
def test_parents_meeting_info(parent_page):
    """https://testlink.it.ru/education/school-615
    """
    meeting_time = '17:00'

    meetings_form = parent_page.menu.click(Meetings)
    meetings_form.select_meeting()

    with report.step('Check that meeting will be at %s' % meeting_time):
        assert_that(meetings_form.info_label, contains(meeting_time), 'Meeting mismatched')
