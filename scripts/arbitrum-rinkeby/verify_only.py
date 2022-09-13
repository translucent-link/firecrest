from brownie import FluxAggregator, AcceptAllValidator, accounts


def main():
    acceptAllValuesValidator = AcceptAllValidator.at(
        "0x540358C4386FE3d2cbBDE1396cCBf78386715777")
    fluxAggregator = FluxAggregator.at(
        "0xb31D7B0B80220776Fb38c0d6cf68feAc5b322006")

    # verify contracts
    AcceptAllValidator.publish_source(acceptAllValuesValidator)
    FluxAggregator.publish_source(fluxAggregator)
