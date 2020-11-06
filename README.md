# This is a pytest automation test on the Zoopla.uk website
UI test case:

```gherkin
Scenario: Basic DuckDuckGo Search
    Given the DuckDuckGo home page is displayed
    When the user searches for "panda"
    Then the search result title contains "panda"
    And the search result query is "panda"
    And the search result links pertain to "panda"
```

## Chapter 2: Setting Up pytest

*Example Branch: example/2-pytest-setup*

Let's implement the test using pytest.
Create a new file named `test_search.py` under the `tests` directory,
and add the following code:

```python
"""
These tests cover DuckDuckGo searches.
"""

def test_basic_duckduckgo_search():

    # Given the DuckDuckGo home page is displayed
    # TODO

    # When the user searches for "panda"
    # TODO

    # Then the search result title contains "panda"
    # TODO
    
    # And the search result query is "panda"
    # TODO
    
    # And the search result links pertain to "panda"
    # TODO

    raise Exception("Incomplete Test")
```

