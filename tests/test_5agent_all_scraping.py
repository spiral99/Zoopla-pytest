from pages.agent_all_property_page import ZooplaAllAgentsProperty


def test_agent_all_scraping(browser):
    all_property = ZooplaAllAgentsProperty(browser)
    # verify that the right agent was selected

    all_property.load()

    all_property.annoying()

    e = all_property.title()
    assert e == "Knight Frank - Bristol Sales"

    # # scrape data from all the agent pages
    # all_property.scrap()
    # testing next button

    all_property.scrap()
