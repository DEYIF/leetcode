# 3. 无重复字符的最长子串 中等
# 给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。

# 示例 1:

# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:

# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:

# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 

# 提示：

# 0 <= s.length <= 5 * 104
# s 由英文字母、数字、符号和空格组成
from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        que = deque()
        res = 0
        for i in s:
            while i in que:
                res = max(res, len(que))
                que.popleft()
            que.append(i)
            res = max(res, len(que))
        return res

solution = Solution()
s = "abcabcbb"
print(solution.lengthOfLongestSubstring(s))