
from brownie import FluxAggregator, accounts


def main():
    acct = accounts.load('deployer')
    fluxAggregator = FluxAggregator.at(
        "0x84b3eC007A986DCDd356D7b503A19B30329Fe56d")

    # the list of addresses for the new Oracles being removed,
    # the addresses refer the Node Addresses, NOT oracle/operator contract addresses
    removed = []

    # the list of addresses for the new Oracles being added
    # the addresses refer the Node Addresses, NOT oracle/operator contract addresses
    added = []

    # the admin addresses for the new respective `added` list.
    # Only this address is allowed to access the respective oracle's funds, typically a MM wallet address
    addedAdmins = []

    # the new minimum submission count for each round
    minSubmissions = 1

    # the new maximum submission count for each round
    maxSubmissions = 1

    # the number of rounds an Oracle has to wait before they can initiate a round
    restartDelay = 0

    fluxAggregator.changeOracles(
        removed,
        added,
        addedAdmins,
        minSubmissions,
        maxSubmissions,
        restartDelay,
        {'from': acct}
    )
