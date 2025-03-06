from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        buckets = dict()
        for num, count in counter.items():
            if count in buckets:
                buckets[count].append(num)
            else:
                buckets[count] = [num]
        topk =[]
        for count in range(len(nums),0,-1):
            if count in buckets:
                topk += buckets[count]
            if len(topk) >= k:
                return topk[0:k]
        return topk[0:k]

# from collections import defaultdict
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         dic = defaultdict(int)
#         for num in nums:
#             dic[num] += 1
#         item = dic.items()
#         item = sorted(item,key = lambda x: x[1],reverse = True)
#         res = []
#         for i in range(k):
#             res.append(item[i][0])
#         return res


nums = [1,1,2,2,3]
k = 2
solution = Solution()
print(solution.topKFrequent(nums,k))