# 438. 找到字符串中所有字母异位词 中等
# 给定两个字符串 s 和 p，找到 s 中所有 p 的异位词的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

# 示例 1:
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

#  示例 2:
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
 
# 提示:
# 1 <= s.length, p.length <= 3 * 104
# s 和 p 仅包含小写字母

from typing import List
from collections import deque,defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dicp = defaultdict(int)
        dics = defaultdict(int)
        res = {}
        que = deque()
        for i in p:
            dicp[i] += 1
        for index,i in enumerate(s):
            que.append(i)
            dics[i] += 1
            if len(que) > len(p):
                dics[que[0]] -= 1
                if dics[que[0]] == 0:
                    dics.pop(que[0],None)
                que.popleft()
            if dics == dicp:
                res[index-len(p)+1] = i
                dics[que[0]] -= 1
                if dics[que[0]] == 0:
                    dics.pop(que[0],None)
                que.popleft()
        return list(res.keys())
    
solution = Solution()
s = "cbaebabacd"
p = "abc"
print(solution.findAnagrams(s,p))