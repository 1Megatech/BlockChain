import hashlib as hasher
import datetime as date
import sys
import sqlite3


version = byte(0x00)
walletFile = "wallet.dat"
addressChecksumLen = 4
total = []

# Wallet stores private and public keys
class Wallet:
	def __init__(self, PrivateKey, publicKey):
		self.PrivateKey = PrivateKey
		self.publicKey = PublicKey

# NewWallet creates and returns a Wallet

def NewWallet():
	private, public = newKeyPair()
	wallet = Wallet(private, public)
	return wallet

walletObj = Wallet(1,1)

# GetAddress returns wallet address
def GetAddress():
	pubKeyHash = HashPubKey(walletObj.PublicKey)
	versionedPayload.append(pubKeyHash)
	checksum = checksum(versionedPayload)
	fullPayload.append(checksum)
	address = Base58Encode(fullPayload)
	return address

# HashPubKey hashes public key

def HashPubKey(pubkey = []):
	publicSHA256 = sha256.Sum256(pubKey)
	RIPEMD160Hasher = ripemd160.New()
	err = RIPEMD160Hasher.Write(publicSHA256)
	if err != "":
		print("theres some error")

	publicRIPEMD160 = RIPEMD160Hasher.Sum("")
	return publicRIPEMD160

# ValidateAddress check if address if valid
def ValidateAddress(address):
	pubKeyHash = Base58Decode(address)
	actualChecksum = pubKeyHash[len(pubKeyHash)-addressChecksumLen]
	version = pubKeyHash[0]
	pubKeyHash = pubKeyHash[1 : len(pubKeyHash)-addressChecksumLen]
	targetChecksum = checksum(total.extend(version, pubKeyHash))

	return actualChecksum == targetChecksum

# Checksum generates a checksum for a public key
def checksum(payload = []):
	firstSHA = sha256.Sum256(payload)
	secondSHA = sha256.Sum256(firstSHA[:])
	return secondSHA[:addressChecksumLen]
	


def newKeyPair():
	curve = elliptic.P256()
	private, err = ecdsa.GenerateKey(curve, rand.Reader)
	if err != "":
		print("there is some error")

	pubKey.append(private.PublicKey.X.Bytes(), private.PublicKey.Y.Bytes())
	return private, pubkey 











