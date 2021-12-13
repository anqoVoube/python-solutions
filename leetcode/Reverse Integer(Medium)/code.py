#Instruction: https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = str(abs(x))[::-1]
            x = int("-" + x)
            if -2**31 < x:
                return x
            else:
                return 0
        elif x == 0:
            return 0
        else:
            x = str(x)[::-1]
            x = int(x)
            if x < 2**31 - 1:
                return x
            else: 
                return 0