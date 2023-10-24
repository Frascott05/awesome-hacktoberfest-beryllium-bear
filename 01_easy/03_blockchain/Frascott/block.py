import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "Blocco Genitore")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_index = previous_block.index + 1
        new_block = Block(new_index, previous_block, data)
        self.chain.append(new_block)

# Example usage:
blockchain = Blockchain()

while(True):
    transaction = input("Insert your transaction or press exit to terminate the programm: ")
    if transaction != "exit":
        blockchain.add_block(transaction)
    else:
        print("Arrivederci")
        break

# Display the blockchain
for block in blockchain.chain:
    print(f"Block {block.index} - Data: {block.data}")
