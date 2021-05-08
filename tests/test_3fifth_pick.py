from pages.fifth_pick import ZooplaResultFifthPick


def test_select_highest_price(browser):
    select_highest_price = ZooplaResultFifthPick(browser)

    # load the correct page to be tested
    select_highest_price.load()

    # remove annoying cookies notification
    select_highest_price.annoying()

    # When user is on the result page click on dropdown
    select_highest_price.dropdown_click()

    # When user is on the result page verify the price value to be clicked.
    label = "Highest price"
    assert label == select_highest_price.select_highest_price_value()

    # click on the highest price
    select_highest_price.click_highest_price()

    # click on the the fifth item
    select_highest_price.click_on_fifth_item()
