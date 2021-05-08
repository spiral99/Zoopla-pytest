from pages.agent_pick import ZooplaAgent


def test_agent_pick(browser):
    all_agent = ZooplaAgent(browser)

    all_agent.load()

    all_agent.annoying()

    # store value of the agent name

    f = all_agent.agent_name()
    assert f == "Knight Frank - Bristol Sales"

