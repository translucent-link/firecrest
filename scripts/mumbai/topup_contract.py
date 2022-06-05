
from brownie import LinkToken, FluxAggregator, accounts


def main():
    acct = accounts.load('deployer')
    linkToken = LinkToken.at("0x326C977E6efc84E512bB9C30f76E30c160eD06FB")
    fluxAggregator = FluxAggregator.at(
        "0x84b3eC007A986DCDd356D7b503A19B30329Fe56d")

    paymentAmount = 5 * pow(10, 18)  # 5 LINK
    linkToken.transferAndCall(
        fluxAggregator, paymentAmount, b'', {"from": acct})
