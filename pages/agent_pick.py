"""
This module collecting the agent's name then clicks on the
'See all property to rent from this agent' scrap text from the page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ZooplaAgent:
    # URL

    URL = 'https://www.zoopla.co.uk/for-sale/details/55184792/?search_identifier=e77bec8af2a5edee750e6521ed31ebcd'

    # Locators
    COOKIES_FORM = (By.CSS_SELECTOR, ".ui-cookie-consent-main")
    ACCEPT_COOKIES = (By.CSS_SELECTOR, ".ui-cookie-accept-all-medium-large")
    AGENT = (By.CSS_SELECTOR, ".css-e13akx-Heading3-AgentHeading")
    SELECT_ALL_PROPERTY = (By.LINK_TEXT, "View agent properties")

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def load(self):
        self.browser.get(self.URL)

    def annoying(self):
        if self.browser.find_element(*self.COOKIES_FORM):
            cookie_accept = self.browser.find_element(*self.ACCEPT_COOKIES)
            cookie_accept.click()
        else:
            raise Exception('still showing annoying cookies')

    def agent_name(self):
        heading = self.browser.find_element(*self.AGENT).text
        return heading[:-23]

    def agent(self):
        action = ActionChains(self.browser)
        link = self.browser.find_element(*self.AGENT)
        action.click(on_element=link)
        action.perform()

    def select_all_property(self):
        select_all = self.browser.find_element(*self.SELECT_ALL_PROPERTY)
        select_all.click()
