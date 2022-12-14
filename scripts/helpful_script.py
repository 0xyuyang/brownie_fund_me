from brownie import accounts, network, config, MockV3Aggregator

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]

DECIMALS = 8
# This is 2,000
INITIAL_VALUE = 200000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):

        return accounts[0]

    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")

    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS, INITIAL_VALUE, {"from": get_account()})
