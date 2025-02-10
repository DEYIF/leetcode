# 763. 划分字母区间 中等
# 提示
# 给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
# 注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
# 返回一个表示每个字符串片段的长度的列表。

# 示例 1：
# 输入：s = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。 

# 示例 2：
# 输入：s = "eccbbbbdec"
# 输出：[10]

# 提示：
# 1 <= s.length <= 500
# s 仅由小写英文字母组成
from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        end = 0
        appeared = {}
        for index,i in enumerate(s):
            appeared[i] = index
        for index,i in enumerate(s):
            end = max(end,appeared[i])
            if index == end:
                res.append(end+1)
        for i in range(len(res)-1,0,-1):
            res[i] = res[i] - res[i-1]
        return res
s = s = "ababcbacadefegdehijhklij"
solution = Solution()
print(solution.partitionLabels(s))
        