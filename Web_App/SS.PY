
from BlockChain import BlockChain
from BlockChain import Block
import pickle

import os
if os.path.exists('parrot.pkl'):
    with open('parrot.pkl', 'rb') as f:
        bc = pickle.load(f)
        print(bc.chain)
