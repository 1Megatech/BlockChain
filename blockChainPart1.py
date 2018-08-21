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


#creating a proof-of-work

def proof_of_work(header, difficulty_bits):

    # calculate the difficulty target
    target = 2 ** (256-difficulty_bits) #give difficulty_bits as 24 in here

    for nonce in xrange(max_nonce):
        hash_result = hashlib.sha256(str(header)+str(nonce)).hexdigest()

        # check if this is a valid result, below the target
        if long(hash_result, 16) < target:
            print "Success with nonce %d" % nonce
            print "Hash is %s" % hash_result
            return (hash_result,nonce)

    print "Failed after %d (max_nonce) tries" % nonce
    return nonce


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
num_of_blocks_to_add = 3


'''
first_block = create_genesis_block();
print("genesis block has been created")
print("genesis block previous hash: {}".format(first_block.previous_hash))
print("genesis block hash: {}".format(first_block.hash))
print("genesis block data: {}".format(first_block.data))
'''

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
  block_to_add = next_block(previous_block)
  blockchain.append(block_to_add)
  previous_block = block_to_add
  # Tell everyone about it!

  print("Block #{} has been added to the blockchain!".format(block_to_add.index))
  print("Previous Hash: {}".format(block_to_add.previous_hash))
  print("Hash: {}".format(block_to_add.hash)) 
  print("data: {}\n".format(block_to_add.data))

'''
def run():

	nonce = 0
	print("mining the block containing:".format(block_to_add.data))

	while nonce < sys.maxint:
		block_to_add = next_block(previous_block)
		print("hash value: {}".format(block_to_add.hash))
		if(block_to_add.hash < target)

'''






