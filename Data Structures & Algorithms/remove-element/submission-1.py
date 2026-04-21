class Solution:
    def removeElement(self, nums: List[int], val: int) -> into:
        k = 0
        for el in nums:
            if el != val:
                nums[k] = el
                k = k + 1
        return k
