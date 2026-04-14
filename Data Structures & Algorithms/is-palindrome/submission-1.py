class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned = "".join(c.lower() for c in s if c.isalpha() or c.isalnum())
        return s_cleaned == s_cleaned[::-1]