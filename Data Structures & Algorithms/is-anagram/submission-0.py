class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        inp={}
        for char in s:
            if char in inp:
                inp[char] = inp[char] + 1
            
            else:
                inp[char] = 1
        
        out={}
        for char in t:
            if char in out:
                out[char] = out[char] + 1
            
            else:
                out[char] = 1
        
        return inp == out



        