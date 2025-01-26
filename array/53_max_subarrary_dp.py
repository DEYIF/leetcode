# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 子数组
# 是数组中的一个连续部分。

 

# 示例 1：

# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
# 示例 2：

# 输入：nums = [1]
# 输出：1
# 示例 3：

# 输入：nums = [5,4,-1,7,8]
# 输出：23
 

# 提示：

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
 

# 进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 设dp[i]为以第i个数结尾的连续子序列的最大和
        n = len(nums)
        dp = [-1]*n
        for i,val in enumerate(nums):
            if i >= 1:
                if dp[i-1] <= 0:
                    dp[i] = val
                else:
                    dp[i] = dp[i-1] + val
            else:
                dp[i] = val
        return max(dp)

nums = [-2,1,-3,4,-1,2,1,-5,4]
solution = Solution()
print(solution.maxSubArray(nums))