def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i=0
        j=len(numbers)-1
        while i<j:
            currsum = numbers[i] + numbers[j] 
            if currsum == target:
                return [i+1,j+1]
            elif currsum < target:
                i+=1
            else:
                j-=1
        return []
