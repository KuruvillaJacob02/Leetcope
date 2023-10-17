class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        index = 1
        count = 0
        for i in range(len(nums)-1):
            if (nums[i] != nums[i+1]):
                k+=1
                nums[index] = nums[i+1]
                index+=1
                count = 0
            elif nums[i] == nums[i+1] and count < 1:
                k+=1
                nums[index] = nums[i+1]
                count+=1
                index+=1
        return k+1
