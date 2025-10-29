#count frequency of characters in a string
def count_freq(name:str)->dict:
    hash={}
    for ch in name:
        if hash.get(ch,False):
            hash[ch]+=1
        else:
            hash[ch]=1
    return hash

if __name__=='__main__':
    name='Sooraj'
    print(f'Name: {name}')
    print(count_freq(name))
    