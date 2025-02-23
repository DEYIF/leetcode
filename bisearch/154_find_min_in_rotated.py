from typing import List
from math import inf
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            m = (l+r)//2
            if nums[m] == nums[r]:
                r = r-1
            elif nums[m] < nums[r]:
                r = m
            elif nums[m] > nums[r]:
                l = m+1
        return nums[l]

solution = Solution()
nums = [2,2,2,0,1]
print(solution.findMin(nums))