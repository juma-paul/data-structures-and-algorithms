class Solution:
    def isPalindrome(self, s: str) -> bool:
        self.s = s.lower()
        self.s = re.sub(r'[\W_]+', '', self.s)
        
        left, right = 0, len(self.s) - 1
        
        while left <= right:
            if self.s[left] != self.s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
    
                
        