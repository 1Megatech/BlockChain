import hashlib as hasher
import datetime as date
import sys
import sqlite3

dbFile = "blockchain.db"
blocksBucket = "blocks"
genesisCoinbaseData = "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks"
tip = []


#database connectivity
conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()
#cur.execute('DROP TABLE IF EXISTS blockchain')
cur.execute('CREATE TABLE IF NOT EXISTS blockchain(block INTEGER PRIMARY KEY, transactions TEXT, hash TEXT, prevhash TEXT, nonce INTEGER)')
cur.execute('select count(*) from blockchain')
total = cur.fetchone()[0]

#class Blockchain:
#	def __init__(self, tip):
#		self.tip = tip

# BlockchainIterator is used to iterate over blockchain blocks
class BlockchainIterator:
	def __init__(self, currentHash):
		self.currentHash = currentHash

# MineBlock mines a new block with the provided transactions

def MineBlock(txn = []):
	lastHash = []

	newBlock := NewBlock(transactions, lastHash)
	tip.append(newBlock.hash)


	cur.execute('INSERT INTO blockchain (transactions, hash, prevhash, nonce) VALUES (?,?,?,?)', (newBlock.data, newBlock.hash, newBlock.previous_hash, nonce))
    conn.commit()


def FindUnspentTransactions(address):
	unspentTXs = []
	bci = Iterator()

	#here we store blocks ID's in list called "tip"
	for i in range(len(tip)):
		block = blockchain[i]

		for tx in range(block.transactions):
			txID = str(tx.ID)

			Outputs:
				for outIdx in range(tx.Vout):
					if spentTXOs[txID] != "":
						for spentOut in range(spentTXOs[txID]):
							if spentOut == outIdx:
								continue Outputs

						for out in range(tx.Vout):
							unspentTXs.append(tx)

		if tx.IsCoinBase() == False:
			for i in range(tx.Vin):
				if i.CanUnlockOutputWith(address):
					inTXID = str(i.Txid)
					spentTXOs.append(i.Vout)


		if len(block.previous_hash) == 0:
			break

		return unspentTXs


# FindUTXO finds and returns all unspent transaction outputs

def FindUTXO(addres):
	UTXOs = []

	unspentTransactions := FindUnspentTransactions(address)
	for tx in range(unspentTransactions):
		for out in range(tx.Vout):
			if out.CanBeUnlockedWith(address):
				UTXOs.append(out)

	return UTXOs


# FindSpendableOutputs finds and returns unspent outputs to reference in inputs

def FindSpendableOutputs(address, amount):
	unspentOutputs = []
	unspentTXs = FindUnspentTransactions(address)
	accumulated = 0

	work:
		for tx in range(unspentTXs):
			txID = str(tx.ID)

			for outIdx in range(tx.Vout):
				for out in range(tx.Vout):
					if out.CanBeUnlockedWith(address) and accumulated < amount:
						accumulated += out.Value
						unspentOutputs.append(outIdx)

						if accumulated >= amount:
							break work

		return accumulated, unspentOutputs










	






















