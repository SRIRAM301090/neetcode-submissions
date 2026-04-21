class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kMap = {}
        for num in nums:
            if num in kMap:
                kMap[num] = kMap[num] + 1
            else:
                kMap[num] = 1
        
        kMap = dict(sorted(kMap.items(),  key=lambda item: item[1], reverse=True))
        return list(kMap.keys())[:k]
            