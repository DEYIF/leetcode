from typing import List
from math import inf
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [-inf]+nums+[-inf]
        for i in range(1,n+1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i-1
        
solution = Solution()
nums = [2,1]
print(solution.findPeakElement(nums))