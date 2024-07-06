## Explanation of the Solution

1. Initialize the index `i` to 0.
2. Iterate through the array `arr` using a `for` loop with index `i` ranging from 0 to `len(arr) - 2`.
3. Inside the loop, check if three consecutive elements starting from index `i` (`arr[i]`, `arr[i + 1]`, `arr[i + 2]`) are odd numbers (`arr[i] % 2 != 0`, `arr[i + 1] % 2 != 0`, `arr[i + 2] % 2 != 0`).
4. If all three elements are odd, return `True` immediately as we have found three consecutive odds.
5. If the loop completes without finding such a sequence, return `False`.

