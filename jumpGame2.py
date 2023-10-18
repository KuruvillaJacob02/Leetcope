class Solution(object):
    def jump(self, nums):
        jump = 0
        reach = 0
        end = 0
        if len(nums) == 1: return jump
        for i in range (len(nums)):
            reach = max (reach, nums[i] + i)
            if reach >= len(nums)-1:
                jump += 1
                break
            if i == end:
                jump += 1
                end = reach
        return jump
            
        
