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





