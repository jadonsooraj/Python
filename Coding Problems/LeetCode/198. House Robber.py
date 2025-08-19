# M1: DP

 
# M2: Kadane Style DP () most optimised
def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0,0
        for num in nums:
            temp = max(rob1+num,rob2)
            rob1=rob2
            rob2=temp
        return rob2