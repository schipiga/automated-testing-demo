# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"


def test_queue_information(parent_page):
    """https://testlink.it.ru/education/school-392
    """
    queue_form = parent_page.menu.click(Queue)
    queue_form.select_child(1)
    with allure.step('Check that child queue is %s.'):
        assert_that(queue_form.info_text, equal_to(ethalon), 'Mismatched child queue.')


@pytest.fixture.parametrize()
def test_child_scores(parent_page, child_id):
    """https://testlink.it.ru/education/school-592
    """
    scores_form = parent_page.menu.click(Scores)
    scores_form.select_child(child_id)
    scores_form.scores

def test_parents_meeting_info(parent_page):
    """https://testlink.it.ru/education/school-615
    """
    meetings_form = parent_page.menu.click(Meetings)
    meetings_form.select_meeting()