# LeetCode 4: Median of Two Sorted Arrays
# Approach: Merge and Sort
# Time Complexity: O((m + n) log(m + n))
# Space Complexity: O(m + n)

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Merge both input arrays into a single array
        nums3 = nums1 + nums2

        # Sort the merged array
        nums3.sort()

        # Get the length of the merged array
        n = len(nums3)

        # If the length is odd, return the middle element
        if n % 2 != 0:
            median = nums3[n // 2]
            return float(median)
        else:
            # If the length is even, return the average of the two middle elements
            median = (nums3[n // 2] + nums3[(n // 2) - 1]) / 2.0
            return float(median)
