from collections import deque, defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        inque = defaultdict(int)
        que = deque()
        res = 0
        for i in range(len(s)):
            char = s[i]
            que.append(char)
            inque[char] += 1
            while len(inque.keys()) > k:
                inque[que[0]] -= 1
                if inque[que[0]] <= 0:
                    inque.pop(que[0])
                que.popleft()
            res = max(res, len(que))
        return res

s = "eceba"
k = 2
solution = Solution()
print(solution.lengthOfLongestSubstringKDistinct(s,k))