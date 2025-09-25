
import json
import pickle  



def load():

    try:

        with open('bc_voting.pkl', 'rb') as f:
            obj = pickle.load(f)
        #print(obj.chain)
        d=dict({})

        i=1

        for l in obj.chain:
            #print(l.data, l.prev_hash, l.hash)

            d[i]={'data':l.data, 'hash':l.hash, 'prev_hash':l.prev_hash}
            i=i+1

        y = json.dumps(d, indent=4)
        print(y)
        return y
    except:
        return 'No Data Avaialble'
