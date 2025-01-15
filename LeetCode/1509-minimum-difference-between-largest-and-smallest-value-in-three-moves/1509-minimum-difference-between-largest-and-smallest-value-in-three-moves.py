class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        # Sort the array
        nums.sort()

        # Calculate the differences for these scenarios
        diff1 = nums[-1] - nums[3]
        diff2 = nums[-2] - nums[2]
        diff3 = nums[-3] - nums[1]
        diff4 = nums[-4] - nums[0]

        # Return the minimum difference
        return min(diff1, diff2, diff3, diff4)