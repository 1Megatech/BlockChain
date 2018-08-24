import hashlib as hasher
import datetime as date
import sys
import sqlite3

outputTxnObj = TXOutput(1, msg)


class TXOutput:
  def __init__(self, value, PubKeyHash):
    self.Value = value
    self.PubKeyHash = PubKeyHash

    TXOutputList.extend([self.Value, self.PubKeyHash])
#Lock signs the output

def Lock(address):
	pubKeyHash = Base58Decode(address)
	pubKeyHash = pubKeyHash[1 : len(pubKeyHash)-4]
	outputTxnObj.PubKeyHash = pubKeyHash

#IsLockedWithKey checks if the output can be used by the owner of the pubkey
def IsLockedWithKey(pubKeyHash):
	return outputTxnObj.PubKeyHash==pubKeyHash
 #NewTXOutput create a new TXOutput
def NewTXOutput(value, address):
	txo = TXOutput(value, 0)
	txo.Lock(address)

	return txo
#TXOutputs collects TXOutput
class TXOutputs:
  def __init__(self, value, PubKeyHash):
    self.Outputs= O
# Serialize serializes TXOutputs
def Serialize():
	buff = b""
 	enc = gob.NewEncoder(buff)
	err = enc.Encode(outs)
	if err != "":
		Print(err)
	
 	return buff.bytes()

 # DeserializeOutputs deserializes TXOutputs
def DeserializeOutputs(data =[]):
	
 	dec = gob.NewDecoder(bytes.NewReader(data))
	err = dec.Decode(&outputs)
	if err != "":
		Print(err)
	
 	return outputs
