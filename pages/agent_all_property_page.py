"""
This module collects all the property information of the
selected agent.
"""
import sys

from selenium.webdriver.common.by import By


class ZooplaAllAgentsProperty:
    # Locators

    DATA = (By.ID, "main-content")
    NEXT = (By.LINK_TEXT, "Next")
    AGENT_TITLE = (By.XPATH, "//div[@id='breadcrumbs']/strong[1]")
    SCRAPING = (By.XPATH, "//a[@class='listing-results-price text-price']")

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def title(self):
        href = self.browser.find_element(*self.AGENT_TITLE).text
        return href

    def scrap(self):
        sys.stdout = open("/home/{USER}/Desktop/Zoopla_test_Automation/myOutFile.txt", "w")

        while True:
            next_page_btn = self.browser.find_elements(*self.NEXT)
            if len(next_page_btn) < 1:
                urls1 = self.browser.find_elements(*self.SCRAPING)
                urls1 = [url.text for url in urls1]
                for final in urls1:
                    print(final)
                print("no more pages left")
                break
            else:
                houses = self.browser.find_elements(*self.SCRAPING)
                links = [link.text for link in houses]
                for line in links:
                    print(line)

            element = self.browser.find_element(*self.NEXT)
            element.click()

        sys.stdout.close()
