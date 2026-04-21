class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict_list = {}
        max_consecutive = 0

        for val in nums:
            dict_list[val] = True

        for val in nums:
            prev_num = val - 1
            next_num = val + 1
            
            if prev_num not in dict_list:
                count = 1
            
                while next_num in dict_list:
                    next_num += 1
                    count += 1
                max_consecutive = max(max_consecutive, count)

        return max_consecutive
            