#Instruction: https://leetcode.com/problems/integer-to-roman/
class Solution:
    def intToRoman(self, num: int) -> str:
        our_string_answer = ""
        empty_list = []
        one = 1
        full = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V":5, "I": 1}
        not_full = {"CM": 900, "CD": 400, "XC": 90, "XL": 40, "IX": 9, "IV": 4}
        for i in str(num):
            empty_list.append(int(i + "0" * (len(str(num)) - one)))
            one += 1
        for i in empty_list:
            if i not in not_full.values():
                for j in full.keys():
                    if full[j] <= i:
                        our_string_answer += j
                        x = i - full[j]
                        while x != 0:
                            for o in full.keys():
                                if full[o] <= x:
                                    our_string_answer += o
                                    x -= full[o]
                                    break
                        break
                        
                                    
            else:                
                key_list = list(not_full.keys())
                val_list = list(not_full.values())
                # print key with val 100
                position = val_list.index(i)  
                our_string_answer += key_list[position]
        return our_string_answer