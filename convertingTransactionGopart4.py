import hashlib as hasher
import datetime as date
import sys
import sqlite3


subsidy = 10

#transaction parameters
IDList = []
VinList = []
VoutList = []

#Inputtransactions parameters
TXInputList = []
#Outputparameters
TXOutputList = []

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


# SetID sets ID of a transaction
def SetID(txnList = []):
  sha = hasher.sha256()
  sha.update(txnList[0] + 
             txnList[1] + 
             txnList[2])

  return sha.hexdigest()





msg = "python"
inputTxnObj = TXInput(1, 1, msg)
outputTxnObj = TXOutput(1, msg)
txnObj = Transaction(0, [], [])

# CanUnlockOutputWith checks whether the address initiated the transaction
def CanUnlockOutputWith(unlockingData):
  return inputTxnObj.ScriptSig == unlockingData

# CanBeUnlockedWith checks if the output can be unlocked with the provided data
def CanBeUnlockedWith(unlockingData):
  return outputTxnObj.ScriptPubKey == unlockingData 


# NewCoinbaseTX creates a new coinbase transaction
def NewCoinbaseTX(to, data):
  if data == "":
    data = "Reward to " + to

  txin = TXInput(0, -1, data)
  txout = TXOutput(subsidy, to)
  #return Transaction(0, TXInputList, TXOutputList)
  first_transaction = Transaction(0, TXInputList, TXOutputList)

  first_transaction.ID = SetID(first_transaction)
  return first_transaction




# method for FindSpendableOutputs
def FindSpendableOutputs(from_, amount):
  return accountBalance, unSpentoutputs


def IsCoinBase():
  return len(txnObj.Vin) == 1 and len(txnObj.Vin[0].Txid) == 0 && txnObj.Vin[0].Vout == -1





# NewUTXOTransaction creates a new transaction

def NewUTXOTransaction(from_, to, amount):

  inputs = [] # of TXInput type
  outputs = [] # of TXOutput type

  acc, validOutputs = FindSpendableOutputs(from_, amount)

  if acc < amount:
    print("no enough funds")

  # Build list of Input
  for txid in range(validOutputs):
    err = decode(txid)
    if(err != ""):
      print("there is an error")
    else:
      for outs in range(validOutputs):
        for out in range(outs):
          input = TXInput(txid, out, from_)
          inputs.append(input)

  outputs.append(TXOutput(amount, to))

  if acc > amount:
    outputs.append(TXOutput(acc - amount, from_))  #change

  tx = Transaction(0, inputs, outputs)
  tx.ID = SetID(tx)
  return tx








  















