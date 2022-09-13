
from brownie import LinkToken, FluxAggregator, accounts


def main():
    acct = accounts.load('deployer')
    linkToken = LinkToken.at("0x615fBe6372676474d9e6933d310469c9b68e9726")
    fluxAggregator = FluxAggregator.at(
        "0xb31D7B0B80220776Fb38c0d6cf68feAc5b322006")

    paymentAmount = 5 * pow(10, 18)  # 5 LINK
    linkToken.transferAndCall(
        fluxAggregator, paymentAmount, b'', {"from": acct})
