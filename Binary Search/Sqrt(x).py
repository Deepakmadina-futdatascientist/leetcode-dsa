class Solution(object):
    def mySqrt(self, x):
        first=1
        last=x
        while(first<=last):
            mid=(first+last)//2
            if(mid*mid==x):
                return mid
            elif(mid*mid>x):
                last=mid-1
            elif(mid*mid<x):
                first=mid+1
        return last

        
