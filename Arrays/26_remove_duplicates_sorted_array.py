class Solution(object):
    def removeDuplicates(self, nums):
        """
        Remove duplicates from sorted array in-place
        :type nums: List[int]
        :rtype: int
        """

        duplicates = []

        # collect unique elements
        for x in nums:
            if x not in duplicates:
                duplicates.append(x)

        # copy unique elements back to nums
        for i in range(len(duplicates)):
            nums[i] = duplicates[i]

        # k = number of unique elements
        k = len(duplicates)
        return k
