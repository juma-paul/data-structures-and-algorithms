class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverse the list of characters in place.
        """
        left, right = 0, len(s) - 1  # Initialize two pointers
        while left < right:
            s[left], s[right] = s[right], s[left]  # Swap elements
            left += 1  # Move left pointer right
            right -= 1  # Move right pointer left
    
