"""
This module contains shared fixtures.
"""

import json
import pytest
import selenium.webdriver


@pytest.fixture
def config():
    # Read the file
    with open('D:\\Pytest Automation Framework\\Zoopla_test_Automation\\config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config):
    # Initialize the WebDriver instance

    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()

    elif config['browser'] == 'Safari':
        b = selenium.webdriver.Safari()

    elif config['browser'] == 'Opera':
        b = selenium.webdriver.Opera()

    elif config['browser'] == 'Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('--incognito')
        b = selenium.webdriver.Chrome(options=opts)

    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        opts.add_argument('--incognito')
        b = selenium.webdriver.Chrome(options=opts)

    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait for elements to appear

    b.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup

    yield b

    # Quit the WebDriver instance for the cleanup

    b.quit()
