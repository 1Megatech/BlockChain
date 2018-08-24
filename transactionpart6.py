import hashlib as hasher
import datetime as date
import sys
import sqlite3
import pygob
import random

 subsidy = 10

#transaction parameters
IDList = []
VinList = []
VoutList = []

#Inputtransactions parameters
TXInputList = []
#Outputparameters
TXOutputList = []
#signature list
signList = []


# Transaction represents a Bitcoin transaction
class Transaction:
  def __init__(self, tid, vin = [], vout = []):
    self.ID = tid
    self.Vin = vin
    self.Vout = vout
    
    IDList.append(self.ID)
    VinList.append(list(self.Vin))
    VoutList.append(list(self.Vout))

# TXInput represents a transaction input
class TXInput:
  def __init__(self, txid, vout, scriptSig):
    self.Txid = txid
    self.Vout = vout
    self.ScriptSig = scriptSig

    TXInputList.extend([self.Txid, self.Vout, self.ScriptSig])

# TXOutput represents a transaction output
class TXOutput:
  def __init__(self, value, scriptPubKey):
    self.Value = value
    self.ScriptPubKey = scriptPubKey

    TXOutputList.extend([self.Value, self.ScriptPubKey])


msg = "python"
inputTxnObj = TXInput(1, 1, msg)
outputTxnObj = TXOutput(1, msg)
txnObj = Transaction(0, [], [])


# IsCoinbase checks whether the transaction is coinbase
def IsCoinBase():
  return len(txnObj.Vin) == 1 and len(txnObj.Vin[0].Txid) == 0 && txnObj.Vin[0].Vout == -1


txnobj = Transaction(1, [], [])

# Hash returns the hash of the Transaction
def Hash():

	txin = TXInput(0, -1, data)
  	txout = TXOutput(subsidy, to)
  	txcopy = Transaction(0, TXInputList, TXOutputList)
	hash = sha256.Sum256(txcopy)
	return hash

# Sign signs each input of a Transaction

def Sign(privKey, prevTXs):
	if txnObj.IsCoinbase():
		return

	for vin in range(txnObj.Vin):
		if prevTXs[str(vin.Txid)].ID == "":
			print("ERROR: Previous transaction is not correct")

	txcopy = txnObj.TrimmedCopy()

	for vin in range(txcopy.Vin):
		prevTx = prevTXs[str(vin.Txid)]
		txCopy.Vin[Vin.index(vin)].Signature = ""
		txcopy.Vin[Vin.index(vin)].PubKey = prevTx.Vout[vin.Vout].PubKeyHash
		txCopy.ID = txCopy.Hash()
		txCopy.Vin[Vin.index(vin)].PubKey = ""

		r, s, err = ecdsa.Sign(random.rand(0,1000), privKey, txCopy.ID)
		if err == "":
			print("there is some error")

		signature = signList.extend(bytes(r), bytes(s))
		tx.Vin[Vin.index(vin)].Signature = signature

# String returns a human-readable representation of a transaction

def String():
	lines = []
	notes = "Transaction" + tx.ID
	lines.extend(lines, notes)

	for input in range(txnObj.Vin):
		lines.extend(lines, "Input " + Vin.index(input))
		lines.extend(lines, "TXID " + input.TXID)
		lines.extend(lines, "Out " + input.Vout)
		lines.extend(lines, "Signature " + input.Signature)
		lines.extend(lines, "PubKey " + input.PubKey)
		

	for output in range(txnObj.Vout):
		lines.extend(lines, "Output " + Vout.index(output))
		lines.extend(lines, "value " + output.Value)
		lines.extend(lines, "script " + output.PubKeyHash)

	return lines

# TrimmedCopy creates a trimmed copy of Transaction to be used in signing

def TrimmedCopy():
	inputs = []
	outputs = []

	for vin in range(txnObj.Vin):
		inputs.extend(outputs, TXInput(vin.Txid, vin.Vout, "", ""))

	for vout in range(txnObj.Vout):
		outputs.extend(outputs, TXOutput(vout.Value, vout.PubKeyHash))

	txcopy = Transaction(tx.ID, inputs, outputs)

	return txcopy

# Verify verifies signatures of Transaction inputs
def Verify(prevTXs):
	if txnObj.IsCoinbase():
		return True

	for vin in range(txnObj.Vin):
		if prevTXs[str(vin.Txid)].ID == "":
			print("ERROR: Previous transaction is not correct")

	txCopy := txnObj.TrimmedCopy()
	curve := elliptic.P256()

	for vin in range(txnObj.Vin):
		prevTx = prevTXs[str(vin.Txid)]
		txCopy.Vin[Vin.index(vin)].Signature = ""
		txCopy.Vin[Vin.index(vin)].PubKey = prevTx.Vout[vin.Vout].PubKeyHash
		txCopy.ID = txCopy.Hash()
		txCopy.Vin[Vin.index(vin)].PubKey = ""

		r = 0
		s = 0
		sigLen = len(vin.Signature)
		r = vin.Signature[:(sigLen / 2)]
		s = vin.Signature[(sigLen / 2):]

		x = 0
		y = 0
		keyLen := len(vin.PubKey)
		x = vin.PubKey[:(keyLen / 2)]
		y = vin.PubKey[(keyLen / 2):]

		rawPubKey := ecdsa.PublicKey(curve, x, y)

		if ecdsa.Verify(rawPubKey, txCopy.ID, r, s) == false:
			return False

	return True

# NewCoinbaseTX creates a new coinbase transaction
def NewCoinbaseTX(to, data):
	if data == "":
    	randData = make([]byte, 20)
		err = rand.Read(randData)
		if err != "":
			Print(err)
 		data = fmt.Sprintf("%x", randData)

  	txin = TXInput(0, -1, data)
  	txout = NewTXOutput(subsidy, to)
  	#return Transaction(0, TXInputList, TXOutputList)
  	tx = Transaction("", TXInputList, TXOutputList)

  	tx.ID = tx.Hash()
  	return tx



# NewUTXOTransaction creates a new transaction
def NewUTXOTransaction(from_, to, amount):
	inputs = [] # of TXInput type
  	outputs = [] # of TXOutput type

 	wallets, err = NewWallets()

 	if err != "":
 		print("ERROR: Not enough funds")

  

  	# Build list of Input
  	for txid in range(validOutputs):
    	err = decode(txid)
    	if(err != ""):
     	 print("there is an error")
    	else:
      	for outs in range(validOutputs):
       		for out in range(outs):
       			input = TXInput(txid, out, "", wallet.PublicKey)
         	 	inputs.append(input)

    #// Build a list of outputs
  	outputs.append(NewTXOutput(amount, to))


  	if acc > amount:
    	outputs.append(NewTXOutput(acc - amount, from_))  #change

  	tx = Transaction("", inputs, outputs)
  	tx.ID = tx.Hash()
  	UTXOSet.Blockchain.SignTransaction(tx, wallet.PrivateKey)
  	return tx






		



























