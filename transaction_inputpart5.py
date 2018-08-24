import hashlib as hasher
import datetime as date
import sys
import sqlite3

class TXInput:
  def __init__(self, txid, vout, pubkey,Signature):
    self.Txid = txid
    self.Vout = vout
    self.pubkey = pubkey
    self.Signature=Signature

  
    TXInputList.extend([self.Txid, self.Vout, self.pubkey,self.Signature])
inputTxnObj = TXInput(1, 1, msg)
def UsesKey(pubKeyHash=[]):
	lockingHash = HashPubKey(inputTxnObj.PubKey)
	return lockingHash==pubKeyHash
 	
