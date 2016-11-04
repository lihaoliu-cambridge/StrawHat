class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len = (len(nums1) + len(nums2))
        if total_len & 1 == 0:
            return ((self.findKthOfTwoArrays(nums1, nums2, total_len / 2) + self.findKthOfTwoArrays(nums1, nums2, total_len / 2 + 1))) / 2.0
        else:
            return self.findKthOfTwoArrays(nums1, nums2, total_len / 2 + 1)

    def findKthOfTwoArrays(self, nums1, nums2, k):
        len_nums1, len_nums2 = len(nums1), len(nums2)
        if len_nums1 > len_nums2:
            len_nums1, len_nums2 = len_nums2, len_nums1
            nums1, nums2 = nums2, nums1
        if len_nums1 == 0:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])

        p = min(len_nums1, k / 2)
        q = k - p

        if nums1[p - 1] < nums2[q - 1]:
            return self.findKthOfTwoArrays(nums1[p:], nums2, k - p)
        elif nums1[p - 1] > nums2[q - 1]:
            return self.findKthOfTwoArrays(nums1, nums2[q:], k - q)
        else:
            return nums1[p - 1]
