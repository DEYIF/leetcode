from typing import List
from math import inf
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            m = (l+r)//2
            if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]
            elif nums[m] == nums[m+1]:
                if m/2 == m//2:
                    l = m+1
                else:
                    r = m
            elif nums[m] == nums[m-1]:
                m -= 1
                if m/2 == m//2:
                    l = m+2
                else:
                    r = m
        return nums[l]

solution = Solution()
nums = [1,1,2]
print(solution.singleNonDuplicate(nums))