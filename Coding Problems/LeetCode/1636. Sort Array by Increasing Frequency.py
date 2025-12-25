class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d1={}
        for num in nums:
            if d1.get(num,False):
                d1[num]+=1
            else:
                d1[num]=1
        d2=dict(sorted(d1.items(),key=lambda x:(x[1],-x[0])))

        ans=[]
        for key, value in d2.items():
            while value > 0:
                ans.append(key)
                value-=1

        return ans