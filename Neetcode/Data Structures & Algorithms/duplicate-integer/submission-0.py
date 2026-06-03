class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        duplicate = False
        for num in nums:
            if num in s:
                return True
            else: 
                s.add(num)
        return False
        
        