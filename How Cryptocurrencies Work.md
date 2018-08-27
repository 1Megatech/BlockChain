# How Cryptocurrencies Work (Technical Guide)
Cryptocurrency - “A digital currency produced by a public network, rather than any government, that uses cryptography to make sure payments are sent and received safely”.
## components of cryptocurrencies:
- The data structure (most of the time a blockchain)
- Cryptography
- Rewards for running a nodes
- Decentralized (Peer-to-peer) consensus

## Cryptographic Hash function
It is a mathematical algorithm that maps data of arbitrary size to a bit string of a fixed size (a hash) and is designed to be a one-way function, that is, a function which is infeasible to invert.
There are many cryptographic hash functions, such as SHA-256 or Scrypt, X11 (using 11 different hashing functions).
## Data structure
The data structure is the skeleton of every cryptocurrency. Let’s talk about the most famous one: the blockchain.
### Blocks
Most of the cryptocurrencies are using the blockchain data structure. 
##### Structure of a block:
- previousHash → the hash of the previous block
- timestamp → the date time code
- data → in the case of cryptocurrencies it will contain the transactions
- nonce → an integer (it’s used for mining we will explain it later)
- hash → the hash of the current block calculated like this:
hash = H(previousHash + timestamp + data.toString() + nonce)
// with H(x) the hashing function
// and + to concatenate

**Note** that some cryptocurrencies uses some preffix to their hashes, or addresses to differentiate between each others.
The power of this data structure is that, if you change the data of one block, you will have to re-calculate the hash of the block which will invalidate the value previousHash of the next block.
Note that there is one very special block, the first block, it doesn’t have any previousHash, it’s called the **GenesisBlock**.
The blockchain data structure is used by most of the coins such as **Bitcoin, Litecoin or Ethereum.** 
Any data stored in the blockchain will stay there forever. It can’t hardly be removed.
We can use any technology to store the data structures. Since blocks are identified by their hash, the best solution is a key-value storage. Bitcoin uses **LevelDB**, a key-value storage library.
## Transactions and cryptography
### Transactions
#### *structure of a transaction*
- transactionInputs[] → Array of transactionInput
- transactionOutputs[] → Array of transactionOutput
- id → Hash calculated from the content of transactionInputs[] and transactionOutputs[]
##### transactionOutput:
- address -> Address of the receiver of the transaction
- amount -> Amount of the cryptocurrency to be sent to the address

##### transactionInput:
- transactionOutputId → id / hash of a previous transaction where the output is taken and use as an input
- transactionOutputIndex → index of the output to find the right output from the transactionOutputs[] array

The rule is the following in every transaction the sum of inputs should be equal to the sum of outputs! So what should be done is: if, let’s say Alice, has received 30 and she wants to send 10, she has to send also 20 to herself! This is how bitcoin works in order to verify transactions faster. It avoids checking the full history every time a transaction is issued.

Let’s see what happen in an example:

1. Let’s say there are 3 people, Alice with the address 0xA, John with the address 0xJ, Bob with the address 0xB, these addresses are theirs public keys
2. Alice has 30 COINS (she previously received it from John in the transaction with the id 0x5645464) and Bob has 0 COINS
3. Alice sends 10 COINS to Bob
4. Alice will create a transaction like the following
```sh
// a first transaction output to bob
const txOut1 = {
  amount: 10,
  address: 0xB //bob's address
}
// a second transaction output to alice herself
const txOut2 = {
  amount: 20,
  address: 0xA //Alice's address
}
// a transaction input
// this transactionOutputId is the id of the transaction 0x5645464 where John sent 30 COINS to Alice previously
const txIn = {
  transactionOutputId: 0x5645464, 
  transactionOutputIndex: 0
}
// We can now create a transaction
const tx = {
  transactionOutputs: [txOut1, txOut2]
  transactionInputs: [txIn],
}
// Then we need to calculate a hash of the transactions
// If you want to know more about this you can check this good tutorial that explains the full process: https://lhartikk.github.io/
```

The "wallet" software does this work for us. Once the transaction is created it has to be signed before being broadcast to the nodes to be part of a block.

### Cryptography
Bitcoin as many other cryptocurrencies is using the **Elliptic Curve Digital Signature Algorithm (ECDSA)** to secure the transactions but also to create public keys and private keys.
Every user of bitcoin needs two keys: the private key (secret key) which is generated randomly and the public key which is generated with the help of **ECDSA algorithm** that is used as an address also to receive money.
**Also, note that this algorithm works only one way, you can get a public key from the private key but not a private key from a public key.**
These two keys are used to sign the transaction. Once the transaction is signed it can be broadcasted to the network. 
When a node receives a transaction it checks whether it is valid or not: no double spend, valid account balance, transaction amounts input equals transaction amount output and valid signature. 
Then it adds it to his transaction pool that it’s also shared with other nodes. Then it adds them to blocks.
### Accounts balance
Bitcoin stores outside of the blockchain the transactions that are received by each address and not spent known as **(Unspent Transaction Output)UTxO**.
By summing up all the UTxO we can know the amount left with the user. This UTxO is stored in a database that is managed and updated locally by every node in order to process the transactions and validate them faster without checking the full blockchain.

### Proof of Work, Mining, and Puzzles

How can all the node agree on which block will be the next one on the blockchain? One solution could be to choose every time one node randomly like a lottery. The problem is the following: if one of the nodes, let’s say X, opens 97 other nodes (by running 97 instances of the software for example), he will have the power, and will be able to blacklist some users and for example never accept the transactions of Bob! This is called a **Sybil attack.**
In reallity, bitcoin blockchain adds one block to the blockchain every 10 minutes, and there is not any limit of 3 transactions per block, but a size limit of 1 megabyte per block, and today (13th April of 2018), 10050 bitcoin nodes are running (see the last number here: https://bitnodes.earn.com/). Bitcoin fight against Sybil attack using the Proof of Work consensus.


##### Proof of Work consensus
Nodes have to resolve a computational puzzle. The first who resolves it will be the chosen one, its block will be added to the blockchain.
Here is how the puzzle works. Remember the block structure? it contained a timestamp, data, a nonce and a hash. Mining consists of incrementing the nonce and calculate the hash until it gives a value that starts with a specific number of 0 called **difficulty.**

So once a node finds the nonce that gives the right number of 0, it has to broadcast its block to the network as it will be chosen as the next block of the blockchain. Also, the one who finds the block gets a reward, to motivate people to make the network more secure by running miners.
The more computational power a node has the more chance it has to validate the next block. Which makes harder to control the blockchain, as you need 51% of the computational power of the world to be able to block some transaction and blacklist them. 
Bitcoin was initially designed to be mined with CPU power, so a lot of computers all around the world were mining it. But since the value of bitcoin increased people started to invest more in mining. They started to mine with GPU, then FPGA (Field-Programmable Gate Array, which are some boards very good with SHA 256 calculation), and now Bitcoin miners are using ASIC (Application-specific integrated circuit) which are devices built for mining Bitcoin (and some others) but their only purpose is mining. Mining is costly in hardware (buying it), and it also consumes quite a lot of electricity for running and for cooling. We will talk later about the waste of energy. But that’s the deal. Proof of Work is a way to convert energy and work into coins and security.

Miners usually work together in pools. Pools will make the miners try to find the nonce together. They give rewards based on the number of shares found, a share is a hash which starts with a number of 0 which is a bit inferior to the difficulty level.

### Rewards & transaction fees
As explained above, the reward is an incentive to make users become miners, in order to secure the network. Without miners, the network cannot be secured, and without rewards, no one will want to waste its energy, therefore their money.
In bitcoin every node that validates a block receive currently 12.5 BTC, this amount is halved every 4 years.
Also when you do a transaction you have to set a transfer fee. This fee is collected by miners. If there are too many transactions happening, the miners will take in priority the transactions with more fees. So you will have to pay higher fees to see your transaction happening fast.

### Confirmations & branches
Confirmations are the number of blocks in the blockchain that are after the block containing the transaction. In bitcoin, if a transaction gets more than 6 confirmations it’s considered as secured, and it’s unlikely that it will get orphaned. So if you sell goods or services with bitcoin be sure to get the 6 confirmation before giving their due.

### Challenges faced by cryptocurrencies
- Scalability
- Speed
- Cost
- Centralisation
- Energy waste









