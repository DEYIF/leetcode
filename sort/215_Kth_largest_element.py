from typing import List
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 随机算一个数
        larger, equal, smaller = [], [], []
        pivot = random.choice(nums)
        for i in nums:
            if i > pivot:
                larger.append(i)
            elif i < pivot:
                smaller.append(i)
            else:
                equal.append(i)
        if k <= len(larger):
            return self.findKthLargest(larger,k)
        elif k > (len(larger)+len(equal)):
            return self.findKthLargest(smaller,k-(len(larger)+len(equal)))
        return pivot
    


solution = Solution()
nums = [3,2,1,5,6,4]
k = 2
print(solution.findKthLargest(nums,k))