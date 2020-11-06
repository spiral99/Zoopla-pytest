"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

from selenium.webdriver.common.by import By


class ZooplaResultPage:
    # Locators

    RESULT_LINKS = (By.ID, 'main-content')
    SEARCH_INPUT = (By.ID, "location")

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]

        with open("/home/brian/Desktop/Zoopla_test_Automation/test_output.txt", "w+") as f:
            f.write('\n'.join(titles))

        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        print(value)
        return value

    def title(self):
        return self.browser.title
