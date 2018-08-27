# Building Blockchain in Go. Part 5: Addresses

## Bitcoin Address
 Bitcoin addresses are public. If you want to send coins to someone, you need to know their address. But addresses (despite being unique) are not something that identifies you as the owner of a “wallet”. In Bitcoin, your identity is a pair (or pairs) of private and public keys stored on your computer. Bitcoin relies on a combination of cryptography algorithms to create these keys, and guarantee that no one else in the world can access your coins without getting physical access to your keys.
 
 ## Public-key Cryptography

Public-key cryptography algorithms use pairs of keys: public keys and private keys. Public keys are not sensitive and can be disclosed to anyone. In contrast, private keys shouldn’t be disclosed: no one but the owner should have access to them because it’s private keys that serve as the identifier of the owner. In essence, a Bitcoin wallet is just a pair of such keys. When you install a wallet application or use a Bitcoin client to generate a new address, a pair of keys is generated for you.  Private and public keys are just random sequences of bytes, thus they cannot be printed on the screen and read by a human. That’s why Bitcoin uses an algorithm to convert public keys into a human readable string.

## Digital Signatures

In mathematics and cryptography, there’s a concept of digital signature – algorithms that guarantee:
- that data wasn’t modified while being transferred from a sender to a recipient;
- that data was created by a certain sender;
- that the sender cannot deny sending the data.

Digital signing happens with the usage of a private key, and verification requires a public key.
In order to sign data we need the following things:
- data to sign;
- private key.

In order to verify a signature, the following is required:
- data that was signed;
- the signature;
- public key.

Every transaction input in Bitcoin is signed by the one who created the transaction. Every transaction in Bitcoin must be verified before being put in a block. Verification means (besides other procedures):
- Checking that inputs have permission to use outputs from previous transactions.
- Checking that the transaction signature is correct.

## Elliptic Curve Cryptography
Bitcoin uses elliptic curves to generate private keys. Elliptic curves is a complex mathematical concept, these curves can be used to generate really big and random numbers.
## Base58
 
 Bitcoin uses the Base58 algorithm to convert public keys into human readable format. The algorithm is very similar to famous Base64.
 
## Signatures

Transactions must be signed because this is the only way in Bitcoin to guarantee that one cannot spend coins belonging to someone else. If a signature is invalid, the transaction is considered invalid too and, thus, cannot be added to the blockchain.

