class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
     
        length = len(nums)
        if length < 3:
            return []
        nums = sorted(nums)
        
        if nums[0] > 0 or nums[-1] < 0:
            return []

        for i in range(length - 2):

            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = length - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1

                elif total > 0:
                    k -= 1

                else:
                    ans.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # Skip duplicate j values
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicate k values
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return ans