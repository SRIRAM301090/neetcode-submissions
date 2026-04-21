class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count=0
        counter=0

        for val in nums:
            if val == 0:
                counter = 0
            
            counter = counter + val
            if counter > max_count:
                max_count = counter

        return max_count