# Building Blockchain in Go. Part 6: Transactions 2

## Reward
The miner who mines the block to add it to the blockchain will be rewarded.

## The UTXO Set

chainstate stores the UTXO set, or the set of unspent transaction outputs.
Having the UTXO set means that our data (transactions) are now split into to storages: actual transactions are stored in the blockchain, and unspent outputs are stored in the UTXO set.

## Merkle Tree

Because of the decentralized nature of Bitcoin, every node in the network must be independent and self-sufficient, i.e. every node must store a full copy of the blockchain. With many people starting using Bitcoin, this rule becomes more difficult to follow: it’s not likely that everyone will run a full node.
A Merkle tree is built for each block, and it starts with leaves (the bottom of the tree), where a leaf is a transaction hash (Bitcoins uses double SHA256 hashing). The number of leaves must be even, but not every block contains an even number of transactions. In case there is an odd number of transactions, the last transaction is duplicated (in the Merkle tree, not in the block!).
The benefit of Merkle trees is that a node can verify membership of certain transaction without downloading the whole block. Just a transaction hash, a Merkle tree root hash, and a Merkle path are required for this.
