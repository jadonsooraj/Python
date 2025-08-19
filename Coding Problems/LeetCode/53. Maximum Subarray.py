# M1: Kadane's Algorithm
def maxSubArray(self, nums: list[int]) -> int:
        CurrSum=0 
        MaxSum=nums[0] 
        for num in nums:
            CurrSum = CurrSum + num
            CurrSum = max(CurrSum, num)
            MaxSum = max(MaxSum, CurrSum)
        return MaxSum