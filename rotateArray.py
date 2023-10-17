lass Solution(object):
    def rotate(self, nums, k):
        def reverse(start,end):
            while start < end:
                nums[start],nums[end] = nums[end], nums[start]
                start,end = start+1, end-1
        n = len(nums)
        k %= n
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
