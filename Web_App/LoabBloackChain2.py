
import json
import pickle  



def load(eid):

    try:

        with open('bc_voting.pkl', 'rb') as f:
            obj = pickle.load(f)
        print(obj.chain)
        r=[]
        for l in obj.chain:
            print(l.data[0]['vote'],'<<<<<<<<<<<<<')
            r.append(l.data[0]['vote'])
        print(r)
        r.remove('genesis')
        return r
    except Exception as e:
        print(e)

        return []


if __name__ == '__main__':
    load('1')