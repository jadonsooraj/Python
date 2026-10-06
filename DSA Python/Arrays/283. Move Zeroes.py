class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0

        for mover in range(len(nums)):
            if nums[mover] != 0:
                temp = nums[pointer]
                nums[pointer] = nums[mover]
                nums[mover] = temp
                pointer+=1

                
        
        return nums
                