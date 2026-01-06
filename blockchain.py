import hashlib
import time

class Blockchain:
    def __init__(self):
        self.chain = [self.create_block()]

    def create_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

#Addg a new block
    def add_block(self, data):
        last_block = self.chain[-1]

        new_block = Block(
            index=len(self.chain),
            timestamp=time.time(),
            data=data,
            previous_hash=last_block.hash
        )

        self.chain.append(new_block)

# Validating the blockchain
    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

     # Check current hash
            if current.hash != current.calculate_hash():
                return False

    # Check link to previous block
            if current.previous_hash != previous.hash:
                return False

        return True
