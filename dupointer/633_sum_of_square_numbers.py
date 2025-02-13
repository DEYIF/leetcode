# 633. 平方数之和 中等
# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
 
# 示例 1：
# 输入：c = 5
# 输出：true
# 解释：1 * 1 + 2 * 2 = 5

# 示例 2：
# 输入：c = 3
# 输出：false
 
# 提示：
# 0 <= c <= 231 - 1
from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, h = 0, int(sqrt(c))
        while l <= h:
            temp = pow(l,2) + pow(h,2)
            if temp == c:
                return True
            if temp < c:
                l += 1
            else:
                h -= 1
        return False
c = 5
solution = Solution()
print(solution.judgeSquareSum(c))