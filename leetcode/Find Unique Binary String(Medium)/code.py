#Instruction: https://leetcode.com/problems/find-unique-binary-string/
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        number = nums[0]
        n = 0
        k = []
        s = '0'
        while len(s) <= len(number):
            s = str(bin(n).replace("0b", ""))
            n += 1
        for i in range(n - 1):
            c = str(bin(i).replace("0b", ""))
            if len(c) <= len(number):
                c = '0' * (len(number) - len(c)) + str(bin(i).replace("0b", ""))
                k.append(c)
            else:
                k.append(c)
        
        return (list(set(k) - set(nums)))[0]