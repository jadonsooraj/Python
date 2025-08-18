# M1:Using Hash

def isAnagram(self, s: str, t: str) -> bool:
    if len(s)!=len(t):
        return False
    
    #count hash
    hash={}
    for ele in s:
        hash[ele]=hash.get(ele,0)+1
    #decrement the hash
    for ele in t:
        if ele not in hash:
            return False
        hash[ele]-=1
        if hash[ele]<0:
            return False
    return True

# M2: use counter
    import collections as c
    return c.counter[s]==c.counter[t]

# M3: Use Sorting O(nlogn) assuing no extra space
    return s.sort()==t.sort()