class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        n = len(nums)
        result = []

        # Fix first element
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Fix second element
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1
                new_target = target - nums[i] - nums[j]

                # Two-pointer approach (2Sum)
                while left < right:
                    curr_sum = nums[left] + nums[right]

                    if curr_sum == new_target:
                        result.append([
                            nums[i], nums[j], nums[left], nums[right]
                        ])

                        left += 1
                        right -= 1

                        # Skip duplicates
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif curr_sum < new_target:
                        left += 1
                    else:
                        right -= 1

        return result

---

## Key Takeaway

#Any **k-Sum** problem can be solved by fixing `(k - 2)` elements and applying **2Sum** using two pointers.
