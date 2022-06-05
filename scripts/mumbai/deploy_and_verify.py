from brownie import FluxAggregator, AcceptAllValidator, accounts


def main():
    acct = accounts.load('deployer')

    acceptAllValuesValidator = AcceptAllValidator.deploy({'from': acct})

    # The address of the LINK token
    linkAddress = "0x326C977E6efc84E512bB9C30f76E30c160eD06FB"  # on Polygon Mumbai

    # The amount paid of LINK paid to each oracle per submission, in wei (units of 10⁻¹⁸ LINK)
    # NOTE: This value needs to be higher than MINIMUM_CONTRACT_PAYMENT_LINK_JUELS of the nodes
    # See https://docs.chain.link/docs/configuration-variables/#minimum_contract_payment_link_juels
    oracleFee = 70000000000000000  # 0.07 LINK

    # The number of seconds after the previous round that are allowed to lapse before allowing an oracle to skip an unfinished round
    unfinishedRoundInterval = 30

    # Lower bound of acceptable values
    lowerBound = 0

    # Upper bound of acceptable values
    upperBound = 1000000

    # Represents the number of decimals to offset the answer by
    decimalOffset = 0

    # A short description of what is being reported
    description = "values"

    fluxAggregator = FluxAggregator.deploy(
        linkAddress,
        oracleFee,
        unfinishedRoundInterval,
        acceptAllValuesValidator,
        lowerBound,
        upperBound,
        decimalOffset,
        description,
        {'from': acct}
    )

    # verify contracts
    AcceptAllValidator.publish_source(acceptAllValuesValidator)
    FluxAggregator.publish_source(fluxAggregator)
