"""
This module collects all the property information of the
selected agent.
"""
import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class ZooplaAllAgentsProperty:
    # Locators

    DATA = (By.ID, "main-content")
    NEXT = (By.XPATH, "//div[@id='content']/div[7]/a[5]")
    AGENT_TITLE = (By.XPATH, "//a[@class='listing-results-price text-price']")

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def title(self):
        agent_title = self.browser.find_element(*self.AGENT_TITLE)
        href = agent_title.get_attribute('a href')
        print(href)
        return href

    def click_next(self):
        c_next = self.browser.find_element(By.XPATH, "//div[@id='content']/div[7]/a[5]")
        c_next.click()

    def next(self):
        sys.stdout = open("/home/brian/Desktop/Zoopla_test_Automation/myOutFile.txt", "w+")

        while True:
            self.browser.implicitly_wait(30)
            next_page_btn = self.browser.find_element(By.XPATH, "//div[@id='content']/div[7]/a[5]")
            if len(next_page_btn) < 1:
                # get the last page
                urls1 = self.browser.find_element(By.XPATH, "//a[@class='listing-results-price text-price']")
                urls1 = [url.text for url in urls1]
                for final in urls1:
                    print(final)

                print("no more pages left")
                break
            else:
                urls = self.browser.find_element(By.XPATH, "//a[@class='listing-results-price text-price']")
                urls = [url.text for url in urls]

                for line in urls:
                    print(line)

            action = ActionChains(self.browser)
            element = WebDriverWait(self.browser, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@id='content']/div[7]/a[5]")))
            self.browser.execute_script("return arguments[0].scrollIntoView();", element)
            action.click(on_element=element)
            action.perform()

        sys.stdout.close()
