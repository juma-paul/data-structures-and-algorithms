class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            result.append(num ** 2)
        print(result)
        return sorted(result)