class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(0,n,1):
            nums1[m+i] = nums2[i]
        for i in range(m+n):
            for j in range(m+n-i-1):
                if (nums1[j] >  nums1[j+1]):
                    temp = nums1[j]
                    nums1[j] = nums1[j+1]
                    nums1[j+1] = temp
