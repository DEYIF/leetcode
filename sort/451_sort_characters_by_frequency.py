from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        dic = dict()
        for i,count in counter.items():
            if count in dic:
                dic[count].append(i)
            else:
                dic[count] = [i]
        alpha = []
        for count in range(len(s),0,-1):
            if count in dic:
                alpha += dic[count]
        res = ""
        for i in alpha:
            for k in range(counter[i]):
                res += i
        return res