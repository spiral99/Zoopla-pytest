"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

from selenium.webdriver.common.by import By


class ZooplaResultPage:
    # URL

    URL = 'https://www.zoopla.co.uk/for-sale/property/bristol/?q=Bristol&results_sort=newest_listings&search_source' \
          '=for-sale '

    # Locators
    COOKIES_FORM = (By.CSS_SELECTOR, ".ui-cookie-consent-main")
    ACCEPT_COOKIES = (By.CSS_SELECTOR, ".ui-cookie-accept-all-medium-large")
    RESULT_LINKS = (By.ID, 'main-content')
    SEARCH_INPUT = (By.ID, "header-location")

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

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]

        with open("D:\\Pytest Automation Framework\\Zoopla_test_Automation\\test_output.txt", "w+") as f:
            f.write('\n'.join(titles))

        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        print(value)
        return value

    def title(self):
        return self.browser.title
