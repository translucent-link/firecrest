# Firecrest

A Brownie-based repo for deploying and managing a Chainlink Flux-based decentralised oracle network.

## FluxAggregator Roles & Responsibilities

There are three separate participants involved in the running of a FluxAggregator contract. 

**The Client** - is the owner of the FluxAggregator contract. The Client decides which oracles/node operators to allow in and submit new values to FluxAggregator. The Client also needs to monitor available funds on the contract so that node operators continue to be paid.

**The Node Operator/Admin** - The operator/admin ensures the smooth running of the node and execution of the FluxMonitor job. They need to ensure the node has enough funds in the node wallet to submit new values to FluxAggregator. The node admin is also allowed to withdraw LINK funds paid by the Client held on the FluxAggregator contract. The node admin is identified by a wallet address which for ease-of-use should probably be a Metamask address. 

**The Node** - runs the FluxMonitor jobspec, querying datasources, producing a value, and writing the latest answer to the blockchain. The frequency with which the node writes updates back to the blockchain is controlled through the jobspec.

The FluxAggregator contract could be deployed by any of the initial node operators involved in the project but ownership should be transferred to the client, represented by the client's associated wallet used for LINK topup payments. Technical personell on the client's side should familiarise themselves with the day-to-day responsibilities of running the FluxAggregator contract.

## Environment Variables

You need to setup a .env file in this folder to support the indidual scripts.

    WEB3_INFURA_PROJECT_ID=...
    ETHERSCAN_TOKEN=...
    POLYGONSCAN_TOKEN=...
    ARBISCAN_TOKEN=...

## Before you start

These instructions will be focusing on a deploy to Mumbai, Polygon's test network, identified in Brownie as `polygon-test`. To see a list supported networks

    brownie networks list

You need to setup a "deployer" account

    brownie accounts new deployer
    <you'll now be asked for the private key>

# Deployment

## Step 1. Deploy & Verify

The first step is to deploy the contract to the blockchain, e.g. on Polygon Mumbai. This step is followed by verification, which ensures that the sourcecode of deployed contract is visible for all to see on Polyscan (or Etherescan). Verification also allows you to interact with the contract and see its current state on sites like Polyscan and Etherscan.

To deploy & verify run:

    brownie run scripts/mumbai/deploy_and_verify.py --network polygon-test
    brownie run scripts/arbitrum-rinkeby/deploy_and_verify.py --network arbitrum-rinkeby

## Step 2. Fund FluxAggregator contract

Next you'll need to fund the FluxAggregator contract before you can add node operators, permitting them to submit updates:

    brownie run scripts/mumbai/topup_contract.py --network polygon-test
    brownie run scripts/arbitrum-rinkeby/topup_contract.py --network arbitrum-rinkeby

## Step 3. Add Node Operators & Permissions

Next you need to grant access to allow your node to submit values to the FluxAggregator.

    brownie run scripts/mumbai/manage_nodes.py --network polygon-test
    brownie run scripts/arbitrum-rinkeby/manage_nodes.py --network arbitrum-rinkeby

You'll need to customise the `manage_nodes.py` script every time you run it. For example to add a node operator you need populate the `added` and `addedAdmins` address lists.

The `added` list specifies the new node addresses that are to be granted permission. If you're not adding new addresses, leave the list empty `[]`.
The `addedAdmins` list specifies the admin wallets of the node operators, eg. a Metamask wallet, that the node operator will use to retrieve the LINK payments they've earned. If you're not adding new admins addresses, leave the list empty `[]`.

You can use the `removed` list to specify node addresses from whom you want to remove permission to submit feed updates.

## Step 4. Deploy the FluxMonitor jobspec

Finally, you can now deploy the FluxMonitor job on each node involved in the network. There are example jobspecs in this repository. The most important jobspec property to get right is `contractAddress` property which should point to the FluxAggregator contract address.

# Ongoing Maintenance.

To continue to fund the FluxAggregator contract use the topup_contract.py script which will transfer 5LINK to the FluxAggregator contract everytime its run.

Node Operators should monitor the ETH balance and incorporate the metric into their alerting systems. Node operators will repeatedly need to use their configured wallet to retrieve awarded LINK funds, swap them into ETH, and fund their nodes again.

## Troubleshooting

### Insufficient Funds For Payment
When you run the `manage_nodes.py` script and encounter the following error:

    Gas estimation failed: 'execution reverted: insufficient funds for payment'

You need to fund the FluxAggregator contract with LINK such that the oracles you employ can be paid. The formula is 

    MIN_LINK_REQUIRED = noOracles * oracleFee * 2 rounds
    e.g
                        3 oracles * 0.07LINK * 2 rounds = 0.42 LINK
    
Please use the provided flux_topup.py script, which calls the FluxTopup helper contract to transfer funds to the FluxAggregrator.

### No job runs and console reports: not eligible to submit

If after deploying the job you don't see and job runs appearing in the Job Run tab of the GUI, check the CL node's console for errors. If you come across the following error: `not eligible to submit` you might have submitted the wrong *node address* to the FluxAggregator contract.

### Not topping up contract with LINK, console reports: aggregator is underfunded

The Client needs to ensure that the FluxAggregator contract has enough funds to pay the oracles. The error indicates the contract has run out out funds.

## Credits

Firecrest photo by Alex Lours - [Original](https://en.wikipedia.org/wiki/Common_firecrest#/media/File:Common_firecrest_Franconville_03.jpg)