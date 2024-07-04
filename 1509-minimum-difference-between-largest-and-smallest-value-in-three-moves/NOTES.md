## Explanation of Solution
1. If the length of `nums` is less than or equal to 4, return 0.
2. Sort the array `nums`.
3. Calculate four possible minimum differences by changing up to three elements in different scenarios:
  - Change the three largest elements.
  - Change the two largest and the smallest element.
  - Change the largest and the two smallest elements.
  - Change the three smallest elements.
4. Return the minimum of these differences.
​
