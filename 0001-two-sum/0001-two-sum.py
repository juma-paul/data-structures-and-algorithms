class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        
        for idx, val in enumerate(nums):
            delta = target - val
            if delta in hash:
                return [hash[delta], idx]
            hash[val] = idx
            
        