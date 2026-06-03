class Solution:
    def isPalindrome(self, s: str) -> bool:
        small = "".join(char.lower() for char in s if char.isalnum())
        return small == small[::-1]
            
