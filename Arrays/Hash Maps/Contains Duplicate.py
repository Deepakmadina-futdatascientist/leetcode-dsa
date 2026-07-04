class Solution(object):
    def containsDuplicate(self, nums):
        seen=set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                return True 
        if len(seen)==len(nums):
            return False
           
            
