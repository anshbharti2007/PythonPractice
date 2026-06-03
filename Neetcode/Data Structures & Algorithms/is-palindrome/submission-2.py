class Solution:
    def isPalindrome(self, s: str) -> bool:
        small = ("").join(char.lower() for char in s if char.isalnum())
        reverse_small = small[::-1]
        if small != reverse_small:
            return False
        return True
