from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        m = len(nums)
        i, j = 0, m - 1
        
        res = [0] * m
        for a in range(m - 1, -1, -1):
            if abs(nums[i]) > abs(nums[j]):
                sqr = nums[i]
                i += 1
            else:
                sqr = nums[j]
                j -= 1
            res[a] = sqr * sqr
        return res
            