class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        result = 0

        for el in operations:
            if el == "+":
                record = stack[-1] + stack[-2]
                stack.append(record)
                result += record
            
            elif el == "C":
                result -= stack[-1]
                stack.pop()
            
            elif el == "D":
                record = 2 * stack[-1]
                stack.append(record)
                result += record

            else:
                record = int(el)
                stack.append(record)
                result += record

        return result        