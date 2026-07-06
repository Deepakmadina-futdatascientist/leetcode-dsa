firstBad = 4

def isBadVersion(version):
    return version >= firstBad
                                            #creating fake api to test the code

class Solution(object):
    def firstBadVersion(self, n):
        first = 1
        last = n

        while first < last:
            mid = (first + last) // 2

            if isBadVersion(mid):
                last = mid
            else:
                first = mid + 1

        return first


obj = Solution()
print(obj.firstBadVersion(8))
