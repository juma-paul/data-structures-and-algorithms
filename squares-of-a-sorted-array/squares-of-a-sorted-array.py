class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        last = len(nums) - 1
        result = [0] * len(nums)
        position = last
        
        left, right = 0, last
        
        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            
            if left_square > right_square:
                result[position] = left_square
                left += 1
            else:
                result[position] = right_square
                right -= 1
                
            position -= 1
                
        return result