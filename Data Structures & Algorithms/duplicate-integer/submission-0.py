class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memory ={}

        for val in nums:

            if val in memory:
                return True
            
            memory [val] = True
        
        return False
            
        