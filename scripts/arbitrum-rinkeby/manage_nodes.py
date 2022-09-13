
from brownie import FluxAggregator, accounts


def main():
    acct = accounts.load('deployer')
    fluxAggregator = FluxAggregator.at(
        "0xb31D7B0B80220776Fb38c0d6cf68feAc5b322006")

    # the list of addresses for the new Oracles being removed,
    # the addresses refer the Node Addresses, NOT oracle/operator contract addresses
    removed = []

    # the list of addresses for the new Oracles being added
    # the addresses refer the Node Addresses, NOT oracle/operator contract addresses
    added = ["0x6cf2662e26528ECa524560C2261dDeED550b3f09"]

    # the admin addresses for the new respective `added` list.
    # Only this address is allowed to access the respective oracle's funds, typically a MM wallet address
    addedAdmins = ["0xEB562F4b862E3D7c7Dd306d9a26dE98660390310"]

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
