"""
This module clicks on the fifth item on the 
list selected by highest price.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ZooplaResultFifthPick:
    # URL

    URL = 'https://www.zoopla.co.uk/for-sale/property/bristol/?q=Bristol&results_sort=newest_listings&search_source' \
          '=for-sale '

    # Locators
    COOKIES_FORM = (By.CSS_SELECTOR, ".ui-cookie-consent-main")
    ACCEPT_COOKIES = (By.CSS_SELECTOR, ".ui-cookie-accept-all-medium-large")
    DROPDOWN_ELEMENT = (By.XPATH, "//select[@id='sort-order-dropdown']")
    SELECT_HIGHEST_PRICE = (By.XPATH, "//select[@id='sort-order-dropdown']/option[text()='Highest price']")
    CLICK_HIGHEST_PRICE = (By.XPATH, "//select[@id='sort-order-dropdown']/option[text()='Highest price']")
    FIFTH_ITEM = (By.CSS_SELECTOR, "div:nth-of-type(5) > .css-1ub0h4c-Wrapper-ListingCard-StyledListingCard.e1mc0vr90"
                                   ".e2uk8e10.earci3d1 .css-15tydk8-StyledLink-Link-FullCardLink.e2uk8e4.e33dvwd0")

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

    def dropdown_click(self):
        action = ActionChains(self.browser)
        dropdown = self.browser.find_element(*self.DROPDOWN_ELEMENT)
        action.click(on_element=dropdown)
        action.perform()

    def select_highest_price_value(self):
        select_price = self.browser.find_element(*self.SELECT_HIGHEST_PRICE)
        label = select_price.get_attribute('label')
        print(label)
        return label

    def click_highest_price(self):
        click_highest = self.browser.find_element(*self.CLICK_HIGHEST_PRICE)
        click_highest.click()

    def click_on_fifth_item(self):
        fifth_item = self.browser.find_element(*self.FIFTH_ITEM)
        fifth_item.click()
