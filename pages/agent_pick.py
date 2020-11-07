"""
This module collecting the agent's name then clicks on the
'See all property to rent from this agent' scrap text from the page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ZooplaAgent:
    # Locators

    AGENT = (By.CSS_SELECTOR, ".ui-agent:nth-child(1) .ui-agent__name")
    SELECT_ALL_PROPERTY = (By.LINK_TEXT, "See all property for sale from this agent")

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def agent_name(self):
        heading = self.browser.find_element(*self.AGENT).text
        return heading

    def agent(self):
        action = ActionChains(self.browser)
        link = self.browser.find_element(*self.AGENT)
        action.click(on_element=link)
        action.perform()

    def select_all_property(self):
        select_all = self.browser.find_element(*self.SELECT_ALL_PROPERTY)
        select_all.click()
