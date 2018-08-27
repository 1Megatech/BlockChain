# Proof of What? Understand the Distributed Consensuses in Blockchain

## Why consensus is needed?
The main purpose of consensus is to decide which transaction should be included in the blockchain.
But which one to choose?
One solution could be to choose every time one node randomly like a lottery.
But the problem is that "if one node say X, opens 97 other nodes (by running 97 instances of a software i.e; like DDoS attack) then he/she will have the power and will be able to backlist some users and for example, never accept the transactions of Bob. This is called **Sybil attack**".
But in reality, bitcoin blockchain addsone block of the blockchain every 10 minutes and there are no limits, but a size limitof 1 megabyte per block.
Bitcoin against sybil attack using **proof of work** consensus.

## Proof of Work
More the computation power, more chances you have to find block. This working process is called "Mining" and consumes a lot of electricity.
- Most of then uses blockchain data structure.
- Nano(Raiblock) uses "block lattices"(one blockchain per account)
- IOTA uses Tangle

## Proof of stake

The more coins you stake(own in your account) the more chances you have to find the next block.
Some cryptocurrencies takes into account the age of coin, how long the coins are been staked in the account.
Some cryptocurrencies ask's to maintain minimum balance to be able to stake.
process of finding a block is known as **forging**
Basically instead of buying equipment, we can buy coins and keep them online. We require no calculationsa exceptchecking the validity of transactionsand we can run these cryptocurrencies even on raspberryPie
These coins can be compared with stocks and dividends. We can find annual rates and these rates will decrease year-by-year.
**PeerCoin** is the first cryptocurrency who uses POS.

## Delegated POS
The more coins you have the more voting power you have to select the nodes who are going to validate the next block. It is like democracy. The one who can vote are called **delegates**
If nodes are acting malicious, they will not be electes again. That's how DPOS protects hte network.
BitShares is an example of DPOS

## Proof of capacity

The more disk space you have the more chance you have to mine the next block.
It's energy efficient
Burstcoin is the first and the only Proof of Capacity cryptocurrency.
It even works with a Raspberry Pi and solar electricity.

## Proof of Space and Time (PoCT)

Proof of Space and Time is similar to Proof of Capacity. The “Space” and “Capacity” have actually the same meaning! It just adds another parameter, the time, I would say the time of staking. It is also energy efficient.
There is only one coin made by BitTorrent founders, and it is still work in progress: Chia.

## Distributed Acyclic Graph (DAG / Tangle)
The DAG is a data structure different than a blockchain. It doesn’t use any blocks. It’s a lot of interlinked transactions. To put it simply, when a user, Alice, does a transaction, she will validate two previous transactions. Since it’s not using any mining it’s also energy efficient.
**Iota and Byteball** are the two cryptocurrencies uses this structure.

## Practical Byzantine Fault Tolerance (PBFT)

In PBFT every node has to communicate to all the other nodes to validate the transactions. It cannot have more than 30 nodes to the network. This consensus can handle 1000 transactions per second.
**Hyperledger, Tendermint** both are blockchain platforms and not currencies which uses PBFT.

## Federated Byzantine Agreement (FBA)

This solution is similar to the previous one but instead of asking all the nodes to validates transactions, a limited group of nodes will work together to validates the transactions.
**Ripple, Stellar** uses FBA consensus.

## Delegated Byzantine Fault Tolerance (DBFT)
This protocol is similar to the Delegated Proof of Stake. It works through the votes of the users, to select the nodes they trust. The main difference is that 66% of the delegates have to be in agreement in order to add the block to the blockchain whereas, in DPoS, only one of the delegates is chosen to select the next block.
Neo cryptocurrency is using the DBFT consensus.

## Proof of Authority (PoA)

Only a few known accounts called validators can validate transactions and create the next blocks. It’s very centralized and it’s mostly used by private blockchains.
POA blockchain is using Proof of Authority consensus



