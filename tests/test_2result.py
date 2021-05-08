import pytest

from pages.result import ZooplaResultPage


@pytest.mark.parametrize('phrase', ['Bristol'])
def test_results_page(browser, phrase):
    result_page = ZooplaResultPage(browser)
    result_page.load()
    result_page.annoying()
    assert phrase in result_page.title()
