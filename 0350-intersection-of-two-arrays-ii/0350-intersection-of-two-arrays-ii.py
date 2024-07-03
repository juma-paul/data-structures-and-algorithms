class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_nums2 = Counter(nums2)
        res = []
        
        for num in nums1:
            if count_nums2[num] > 0:
                res.append(num)
                count_nums2[num] -= 1
        return res
        
            
            
        