"""
This module clicks on the fifth item on the 
list selected by highest price.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ZooplaResultFifthPick:
    # Locators

    DROPDOWN_ELEMENT = (By.CSS_SELECTOR, ".listing-results-utils-sortby .js-redirects-to-option:nth-child(3)")
    SELECT_HIGHEST_PRICE = (By.CSS_SELECTOR, ".listing-results-utils-sortby option:nth-child(2)")
    CLICK_HIGHEST_PRICE = (By.CSS_SELECTOR, ".listing-results-utils-sortby option:nth-child(2)")
    FIFTH_ITEM = (By.XPATH, "//li[6]/div/div[2]/a")

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

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
