from typing import List
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key = lambda x: (-len(x),x))
        ps = 0
        pd = 0
        i = 0
        while 1:
            if pd >= len(dictionary[i]):
                return dictionary[i]
            if ps >= len(s):
                ps = 0
                pd = 0
                i += 1
            if i>= len(dictionary):
                return ""
            if pd >= len(dictionary[i]):
                return dictionary[i]
            if s[ps] == dictionary[i][pd]:
                ps += 1
                pd += 1
            else:
                ps += 1
        return ""

solution = Solution()
s = "aaa"
dictionary = ["aaa","aa","a"]
print(solution.findLongestWord(s,dictionary))