import hashlib  
import json  
from time import time  
import pickle  
class Block:  
    def __init__(self, data, prev_hash):  
        self.data = data
        self.prev_hash = prev_hash
        self.hash=self.calc_hash()

    def calc_hash(self):  

        sha=hashlib.sha256()  
        print(str(self.data[0]['citizen'])+str(self.data[0]['eid']))
        sha.update(str(str(self.data[0]['citizen'])+str(self.data[0]['eid'])).encode('utf-8'))
        return sha.hexdigest()
        

class BlockChain:

    def __init__(self):  
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block([{'citizen':'genesis','eid':'genesis','vote':'genesis'}],'00000000')

    def add_block(self, data):
        prev_block=self.chain[-1]
        new_block=Block(data, prev_block.hash)
        self.chain.append(new_block)


if __name__ == '__main__':
    bc=BlockChain()
    bc.add_block([{'citizen':'sajid','eid':'1','vote':'1'}])
    with open('parrot.pkl', 'wb') as f:
        pickle.dump(bc, f)

    """    
    import pickle
    with open('parrot.pkl', 'wb') as f:
        pickle.dump(bc.chain, f)
    with open('parrot.pkl', 'rb') as f:
        mynewlist = pickle.load(f)
    """


    bc.add_block([{'citizen':'nashu','eid':'1','vote':'1'}])
    bc.add_block([{'citizen':'swamy','eid':'1','vote':'1'}])
    