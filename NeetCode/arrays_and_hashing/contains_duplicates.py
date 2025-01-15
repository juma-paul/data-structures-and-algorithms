from typing import List

def has_duplicates_compare(nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
    # TC: O(n^2), SC: O(1)

def has_duplicates_sort(nums: List[int]) -> bool:
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False
    # TC: O(nlogn), O(1)

def has_duplicates_hashset(nums: List[int]) -> bool:
    hash_set = set()
    for i in nums:
        if i in hash_set:
            return True
        hash_set.add(i)
    return False

def has_duplicates_short(nums: List[int]) -> bool:
    return len(set(nums)) < len(nums)
