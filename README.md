# My Blockchain Project

## Description

I made a simple blockchain in Python to understand how they work. It has two main parts - a Block class and a Blockchain class.

## How It Works

Each block stores:
- index (position in chain)
- timestamp 
- data (whatever info you want)
- previous_hash (connects to last block)
- nonce (for mining, not used yet)
- hash (SHA256 of everything)

The blocks connect because each one saves the hash of the previous block. So if you change Block 2, Block 3 will know something's wrong because the hash doesn't match anymore.

## add_block(data)

This function creates and appends a new block to the blockchain.
How it works:
1. Retrieves the last block in the chain
2. Creates a new Block with:
   - Index: current chain length
   - Timestamp: current time
   - Data: the information to store
   - Previous_hash: hash of the last block
3. Appends the new block to the chain


## is_valid
Validation checks:
1. Hash integrity - Recalculates each block's hash and compares it with the stored hash
2. Chain continuity - Verifies each block's previous_hash matches the actual previous block's hash

If someone tampers with any block's data, the stored hash won't match the recalculated hash, and the validation will fail.

## Proof of Work

The current code includes a `nonce` field in the Block structure but does not implement actual mining.


## Tools used
Python (VS code)
hashlib for SHA256
time module  

## References
Youtube tutorials on blockchain in python.
YouTube tutorials on blockchain basics.
