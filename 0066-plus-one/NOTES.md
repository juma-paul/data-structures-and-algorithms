## Explanation of the Solution

1. Start iterating from the last digit (rightmost) to the first digit (leftmost) using a `for` loop.
2. For each digit:
  - If the digit is less than 9, increment it by 1 and return the modified list of digits.
  - If the digit is 9, set it to 0 and continue to the next digit.
3. If all digits were processed and they were all 9, prepend 1 to the list of digits.
4. Return the modified list which now represents the incremented integer.
​
