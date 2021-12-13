#Instruction: https://leetcode.com/problems/array-nesting/
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        dictionary = []
        objects = []
        answer = 0
        k = 0
        for i in range(len(nums)):
            answer = max(answer, k)
            final = nums[i]
            list_of_objects = [final]
            k = 0
            while k < len(nums):
                k += 1
                final = nums[final]
                list_of_objects.append(final)
                if final == nums[i]:
                    dictionary.append(i)
                    answer = max(answer, k)
                    objects += list_of_objects
                    break
                elif final in dictionary or final in objects:
                    break
        return answer
                    