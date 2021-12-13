#Instruction: https://leetcode.com/problems/maximum-matrix-sum/
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        b = []
        d = []
        final_answer = 0
        a = len(matrix)
        for i in range(a):
            for j in range(a):
                final_answer += abs(matrix[i][j])
                b.append(matrix[i][j])
                d.append(abs(matrix[i][j]))
        dappend = sorted(d)
        answer = sorted(b)
        counter = 0
        for i in answer:
            if i <= 0:
                counter += 1     
        if counter % 2 == 0:
            return final_answer
        else:
            return final_answer - 2 * dappend[0]