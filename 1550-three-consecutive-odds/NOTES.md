## Explanation of the Solution

1. Convert the input string `s` to lowercase and remove all non-alphanumeric characters using regular expressions.
2. Initialize two pointers, `left` and `right`, to the first and last indices of the cleaned string, respectively.
3. Iterate through the string using the two pointers until they meet or cross.
4. If the characters at the `left` and `right` pointers are not equal, return `False` as the string is not a palindrome.
5. Otherwise, continue iterating by incrementing the `left` pointer and decrementing the `right` pointer.
6. If the loop completes without returning `False`, the string is a palindrome, so return `True`.​
