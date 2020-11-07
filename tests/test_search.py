"""
These tests cover DuckDuckGo searches.
"""
import pytest

from pages.agent_pick import ZooplaAgent
from pages.agent_all_property_page import ZooplaAllAgentsProperty
from pages.fifth_pick import ZooplaResultFifthPick
from pages.result import ZooplaResultPage
from pages.search import ZooplaSearchPage


@pytest.mark.parametrize('phrase', ['Bristol'])
def test_basic_zoopla_search(browser, phrase):
    search_page = ZooplaSearchPage(browser)
    result_page = ZooplaResultPage(browser)
    select_highest_price = ZooplaResultFifthPick(browser)
    all_property = ZooplaAllAgentsProperty(browser)
    all_agent = ZooplaAgent(browser)

    # Given the home page is displayed
    search_page.load()

    # Remove the annoying cookies notification
    search_page.annoying()

    # When the user searches for "Bristol"
    search_page.search(phrase)

    # Then the search result query is "Bristol"
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to "Bristol"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    # And the search result title contains "Bristol"
    assert phrase in result_page.title()

    # When user is on the result page click on dropdown
    select_highest_price.dropdown_click()

    # When user is on the result page verify the price value to be clicked.
    label = "Highest price"
    assert label == select_highest_price.select_highest_price_value()

    # click on the highest price
    select_highest_price.click_highest_price()

    # click on the the fifth item
    select_highest_price.click_on_fifth_item()

    # store value of the agent name
    f = all_agent.agent_name()

    # click on the agent name
    all_agent.agent()

    # clicks on the 'See all property to rent from this agent'
    all_agent.select_all_property()

    # verify that the right agent was selected
    e = all_property.title()

    assert e == f

    # # scrape data from all the agent pages
    # all_property.scrap()

    # testing next button
    all_property.scrap()
