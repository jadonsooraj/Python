# M1: O(n2)
def twoSum(self, nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j] == target and i!=j:
                return [i,j]

# M2 : 
def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash={} #value:index
        for i, num in enumerate(nums):
            if target - num in hash:
                return [hash[target-num],i]
            hash[num]=i
        return
