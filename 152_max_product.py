# 152. Maximum Product Subarray
# Medium
# Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dpp = [nums[0]]*n   #以i结尾的最大乘积子数组
        dpn = dpp.copy()    #以i结尾的最小乘积子数组
        premax = 0
        premin = 0
        for i in range(1,n):
            val = nums[i]
            premax = dpp[i-1]*val
            premin = dpn[i-1]*val
            dpp[i] = max(premax, premin, val)
            dpn[i] = min(premax, premin, val)
        return max(dpp)

solution = Solution()
nums = [-2,30,-1]
print(solution.maxProduct(nums))