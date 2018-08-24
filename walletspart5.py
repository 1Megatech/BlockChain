import hashlib as hasher
import datetime as date
import sys
import sqlite3
import pygob

walletFile = "wallet_%s.dat"
class Wallets:
	def __init__(self, Wallet):
    self.Wallet = Wallet
    

#NewWallets creates Wallets and fills it from a file if it exists
def NewWallets(nodeID):
	wallets = Wallets[]
	wallets.Wallets = {}
	err = wallets.LoadFromFile(nodeID)

	return wallets, err

ws=Wallets({0:0})	
#CreateWallet adds a Wallet to Wallets
def  CreateWallet():
	wallet = NewWallet()
	address = printf(wallet.GetAddress())

	ws.Wallets[address] = wallet

	return address

 #GetAddresses returns an array of addresses stored in the wallet file
def GetAddresses():

	for address in range (ws.Wallets ):
		addresses = append(addresses,address)
	

    return addresses

#GetWallet returns a Wallet by its address
def GetWallet(address):
	return ws.Wallets[address]

#LoadFromFile loads wallets from the file
def LoadFromFile(nodeID ):
	walletFile = print(walletFile, nodeID)
	if err = os.Stat(walletFile) and  os.IsNotExist(err):
		return err
	

	fileContent, err = ioutil.ReadFile(walletFile)
	if (err != ""): 
		print(err)


	  wallets ={}
	gob.Register(elliptic.P256())
	decoder = gob.NewDecoder(fileContent)
	err = decoder.Decode(wallets)
	if err != "" :
		print(err)
	

	ws.Wallets = wallets.Wallets

	return ""
def SaveToFile(nodeID ):
	content =[]
	walletFile = print(walletFile, nodeID)

	gob.Register(elliptic.P256())

	encoder = gob.NewEncoder(content)
	err := encoder.Encode(ws)
	if err != "":
		print(err)
	

	err = ioutil.WriteFile(walletFile, content.bytes(), 0644)
	if err !="":
		Print(err)
	
