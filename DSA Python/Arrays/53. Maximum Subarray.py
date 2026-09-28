class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        l,r = 0,0

        max_sum = nums[0]
        curr_sum = 0
        while r < len(nums):
            curr_sum = curr_sum + nums[r]

            if max_sum < curr_sum:
                max_sum = curr_sum
            
            while curr_sum < 0 and l<=r:
                curr_sum = curr_sum - nums[l]
                l+=1
            r+=1
        
        return max_sum
        