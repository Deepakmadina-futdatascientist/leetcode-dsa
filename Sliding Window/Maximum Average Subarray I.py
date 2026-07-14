class Solution(object):
    def findMaxAverage(self, nums, k):
        windows_sum=sum(nums[:k])
        max_sum=windows_sum
        for i in range(k,len(nums)):
            windows_sum=windows_sum-nums[i-k]+nums[i]
            max_sum=max(max_sum,windows_sum)
        avg=max_sum/float(k)
        return avg
