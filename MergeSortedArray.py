class Solution(object):
    def merge(self, nums1, m, nums2, n):

        i = m - 1  # Index of the last element in nums1
        j = n - 1  # Index of the last element in nums2
        k = m + n - 1  # Index of the last position in the merged array nums1

        # Merge elements in descending order until one of the arrays is exhausted
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If there are remaining elements in nums2, copy them to nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        return nums1

