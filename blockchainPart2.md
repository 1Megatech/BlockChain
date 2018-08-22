# Dilling

# Introduction

A key idea of blockchain is that one has to perform some hard work to put data in it. It is this hard work that makes blockchain secure and consistent.
This mechanism is very similar to the one from real life: one has to work hard to get a reward and to sustain their life. In blockchain, some participants (miners) of the network work to sustain the network, to add new blocks to it, and get a reward for their work.
It’s worth noting that, the one who finished the work has to prove this.
This whole “do hard work and prove” mechanism is called proof-of-work. It’s hard because it requires a lot of computational power: even high performance computers cannot do it quickly.
One last thing to note. Proof-of-Work algorithms must meet a requirement: doing the work is hard, but verifying the proof is easy. A proof is usually handed to someone else, so for them, it shouldn’t take much time to verify it.

# Hashing
Hashing is a process of obtaining a hash for specified data. A hash is a unique representation of the data it was calculated on. A hash function is a function that takes data of arbitrary size and produces a fixed size hash. Here are some key features of hashing:

- Original data cannot be restored from a hash. Thus, hashing is not encryption.
- Certain data can have only one hash and the hash is unique.
- Changing even one byte in the input data will result in a completely different hash.

In blockchain, hashing is used to guarantee the consistency of a block. The input data for a hashing algorithm contains the hash of the previous block, thus making it impossible (or, at least, quite difficult) to modify a block in the chain: one has to recalculate its hash and hashes of all the blocks after it.

# Hashcash
Bitcoin uses Hashcash, a Proof-of-Work algorithm that was initially developed to prevent email spam. It can be split into the following steps:

- Take some publicly known data (in case of email, it’s receiver’s email address; in case of Bitcoin, it’s block headers).
- Add a counter to it. The counter starts at 0.
- Get a hash of the data + counter combination.
- Check that the hash meets certain requirements.
-- If it does, you’re done.
-- If it doesn’t, increase the counter and repeat the steps 3 and 4.

Thus, this is a brute force algorithm: you change the counter, calculate a new hash, check it, increment the counter, calculate a hash, etc. That’s why it’s computationally expensive.

Now let’s look closer at the requirements a hash has to meet. In the original Hashcash implementation, the requirement sounds like “first 20 bits of a hash must be zeros”. In Bitcoin, the requirement is adjusted from time to time, because, by design, a block must be generated every 10 minutes, despite computation power increasing with time and more and more miners joining the network.

To demonstrate this algorithm, I took the data from the previous example (“I like donuts”) and found a hash that starts with 3 zero-bytes:


```sh
import hashlib as hasher
import datetime as date
import sys

nonce = 0

class Block:
  def __init__(self, index, timestamp, data, previous_hash, nonce):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.nonce = nonce  
    self.previous_hash = previous_hash
    self.hash = self.hash_block()
  
  def hash_block(self):
    sha = hasher.sha256()
    sha.update(str(self.index) + 
               str(self.data) + 
               str(self.previous_hash)+
               str(self.timestamp) + 
               hex(nonce))
    return sha.hexdigest()

#creating genesis Block
def create_genesis_block():
# Manually construct a block with
# index zero and arbitrary previous hash
  return Block(0, date.datetime.now(), "Genesis Block", "0", 0) #last parameter is nonce


#adding blocks one-by-one
def next_block(last_block):
  this_index = last_block.index + 1
  this_timestamp = date.datetime.now()
  this_data = "Hey! I'm block " + str(this_index)
  this_hash = last_block.hash
  this_nonce = last_block.nonce
  return Block(this_index, this_timestamp, this_data, this_hash, this_nonce)


# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# How many blocks should we add to the chain
#  after the genesis block
num_of_blocks_to_add = 2


# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):

  target_bits = 24
  target = 2 ** (256-target_bits)

  nonce = 0

  #we iterate it till the max int value of python
  while nonce < sys.maxint:
    block_to_add = next_block(previous_block)    

    #proof-of-work is calculated here
    #that is if hash value is less than target value, then we add it to the blockchain 
    #since it satisfied the requirements.
    #that is we require 3 bytes of zeros(000000) 6 zeros
    if(long(block_to_add.hash, 16) < target):
      blockchain.append(block_to_add)
      previous_block = block_to_add
      break
    else:
      nonce = nonce + 1
  

  print("Block #{} has been added to the blockchain!".format(block_to_add.index))
  print("Previous Hash: {}".format(block_to_add.previous_hash))
  print("Hash: {}".format(block_to_add.hash)) 
  print("data: {}\n".format(block_to_add.data))
  print("nonce value for block #{}".format(nonce))
```
