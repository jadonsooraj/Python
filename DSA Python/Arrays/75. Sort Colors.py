class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        k = len(nums)-1

            
        while j <= k:
            if nums[j] == 0:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                i+=1
                j+=1
            elif nums[j] == 1:
                j+=1
            else:
                temp = nums[j]
                nums[j] = nums[k]
                nums[k] = temp

                k-=1
                # j+=1
        

         