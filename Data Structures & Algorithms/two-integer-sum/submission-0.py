class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}
        for index,val in enumerate(nums):
            balance = target - val
            if balance in memory:
                return [memory[balance], index]
            else:
                memory[val] = index
        return [-1,-1]

        