# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

# 示例 1：

# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
# 示例 2：

# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
# 示例 3：

# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = {}
        firstdic = {}
        nums.sort()
        n = len(nums)
        for first in range(n):
            if nums[first] in firstdic.values():
                continue
            sum = -nums[first]
            last = n-1
            mid = first+1
            for mid in range(first+1,n):
                if mid > first+1 and nums[mid] == nums[mid-1]:
                    continue
                while mid < last and nums[mid]+nums[last] > sum:
                    last-=1
                if mid == last:
                    break
                if nums[mid] + nums[last] == sum:
                    ans[nums[first],nums[mid],nums[last]] = [first]
            firstdic[first] = nums[first]
        ans = list(ans.keys())
        return ans
solution = Solution()
nums = [-1,0,1,0]
print(solution.threeSum(nums))