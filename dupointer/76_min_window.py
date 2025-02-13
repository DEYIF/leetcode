# 76. 最小覆盖子串    困难
# 提示
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

# 注意：
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。
 

# 示例 1：

# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
# 示例 2：

# 输入：s = "a", t = "a"
# 输出："a"
# 解释：整个字符串 s 是最小覆盖子串。
# 示例 3:

# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。

from collections import defaultdict,deque,Counter
class Solution:
    def isincludet(self, need, t) -> bool:
        count = 0
        for key in need:
            if need[key] >= 0 and key in t:
                count += need[key]
        if count == 0:
            return True
        else:
            return False

    def minWindow(self, s: str, t: str) -> str:
        #队列开头一定是t中的字母
        need = defaultdict(int)
        res = ''
        c = Counter(t)
        temp = len(s)
        if len(s) < len(t):
            return ''
        for i in t:
            need[i] += 1
        #滑动窗口法：如果当前窗口不包含所有t中字符则右侧右移，如果已包含则左侧右移
        l = 0
        r = 0
        while r < len(s):
            while not self.isincludet(need, t):
                if r >= len(s):
                    break
                if s[r] in t:
                    need [s[r]] -= 1
                r += 1
            while self.isincludet(need, t):
                if r-l <= temp:
                    res = s[l:r]
                    temp = len(res)
                need [s[l]] += 1
                l += 1
        return res

s = "acbbaca"
t = "aba"

solution = Solution()
print(solution.minWindow(s,t))
