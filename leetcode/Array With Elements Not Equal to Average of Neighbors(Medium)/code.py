#Instruction: https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        all_in = []
        if len(nums) % 2 == 1:
            number_from_end = int((len(nums) - 1) / 2)
        else:
            number_from_end = int((len(nums) / 2) - 1)
        for i in range(len(nums) - number_from_end, len(nums)):
            all_in.append(nums[i])
        nums = nums[0:len(nums) - number_from_end]
        for i in range(len(all_in)):
            nums.insert(2*i + 1, all_in[i])
        return nums
        
        