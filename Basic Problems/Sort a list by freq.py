#Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

def dict_to_list(d2:dict)->list:
    ans=[]
    for key, value in d2.items():
        while value>0:
            ans.append(key)
            value-=1
    return ans

   
def sort_dict(d1: dict) -> dict:
    return dict(sorted(d1.items(), key=lambda x: (x[1],-x[0])))

if __name__=='__main__':
    nums=[1,1,2,2,2,3]
    d1={}
    for num in nums:
        if d1.get(num,False):
            d1[num]+=1
        else:
            d1[num]=1
    print(d1)
    d1=sort_dict(d1)
    print(dict_to_list(d1))
