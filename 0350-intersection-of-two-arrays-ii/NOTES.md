## Explanation of the Solution

1. Create a `Counter` object `count_nums2` from `nums2` to track element frequencies.
2. Initialize an empty list `res` to collect intersection elements.
3. Iterate through each element `num` in `nums1`.
4. Check if `num` exists in `count_nums2`. If true, append `num` to `res` and decrement its count in `count_nums2`.
5. Return `res`, which contains all elements common to both `nums1` and `nums2` without duplicates.


