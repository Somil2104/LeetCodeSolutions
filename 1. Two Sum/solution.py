class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = {}
        for i, num in enumerate(nums):
            rem = target - num
            if rem in ind:
                return [ind[rem], i]
            ind[num] = i
        
