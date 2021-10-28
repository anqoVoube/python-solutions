class Solution:
    #List -> list, thereby list -> List needed if there occur some error.
    def findMiddleIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            left_corner = 0
            right_corner = 0
            k = i
            c = i
            while i != 0:
                i -= 1
                left_corner += nums[i]
            while k != len(nums) - 1:
                k += 1
                right_corner += nums[k]
            if left_corner == right_corner:
                return c
        return -1
                