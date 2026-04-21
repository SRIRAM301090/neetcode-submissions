class Solution:
    def isValid(self, s: str) -> bool:

        bracket_type = {"}" : "{", "]" : "[", ")" : "("}

        characters = []
        for char in s:
            if char not in bracket_type:
                characters.append(char)

            elif characters and characters[-1] == bracket_type[char]:
                characters.pop()
            
            else:
                return False
        
        return len(characters) == 0 
        