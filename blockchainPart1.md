# Blockchain part 1


# Introduction

Blockchain is one of the most revolutionary technologies of the 21st century, which is still maturing and which potential is not fully realized yet. 

# Block
It stores valuable information. For example bitcoin stores transactions, technical information like version, timestamp, hash of previous block, etc.

Hashing is very important feature if blockchain which makes blockchain more secure. It hash takes variable size input and gives a fixed length output.


# Blockchain
Block is just a database with certain structure i.e; ordered and back-linked list. Which means that blocks are stored in the insertion order and that each block is linked to the previous one. This structure allows to quickly get the latest block in a chain and to (efficiently) get a block by its hash.

To add a new block we need an existing block, but there’re not blocks in our blockchain! So, in any blockchain, there must be at least one block, and such block, the first in the chain, is called genesis block.



```sh
import hashlib as hasher
import datetime as date

class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()
  
  def hash_block(self):
    sha = hasher.sha256()
    sha.update(str(self.index) + 
               str(self.timestamp) + 
               str(self.data) + 
               str(self.previous_hash))
    return sha.hexdigest()


#creating genesis Block
def create_genesis_block():
# Manually construct a block with
# index zero and arbitrary previous hash
  return Block(0, date.datetime.now(), "Genesis Block", "0")




  #adding blocks one-by-one
def next_block(last_block):
  this_index = last_block.index + 1
  this_timestamp = date.datetime.now()
  this_data = "Hey! I'm block " + str(this_index)
  this_hash = last_block.hash
  return Block(this_index, this_timestamp, this_data, this_hash)


  # Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# How many blocks should we add to the chain
#  after the genesis block
num_of_blocks_to_add = 20



  # Add blocks to the chain
first_block = create_genesis_block();
print("genesis block has been created")
print("genesis block previous hash: {}".format(first_block.previous_hash))
print("genesis block hash: {}".format(first_block.hash))
print("genesis block data: {}".format(first_block.data))



for i in range(0, num_of_blocks_to_add):
  block_to_add = next_block(previous_block)
  blockchain.append(block_to_add)
  previous_block = block_to_add
  # Tell everyone about it!

  print("Block #{} has been added to the blockchain!".format(block_to_add.index))
  print("Previous Hash: {}".format(block_to_add.previous_hash))
  print("Hash: {}".format(block_to_add.hash)) 
  print("data: {}\n".format(block_to_add.data))
```
