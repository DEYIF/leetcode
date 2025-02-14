from typing import List
class Solution:
    def firstloc(self, nums, target, loc):
        floc = loc
        while nums[floc] == target:
            floc -= 1
            if floc < 0:
                break
        return floc+1
    
    def lastloc(self, nums, target, loc):
        lloc = loc
        while nums[lloc] == target:
            lloc += 1
            if lloc > len(nums)-1:
                break
        return lloc-1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        res = [-1,-1]
        while l <= r:
            m = int((l+r)/2)
            if nums[m] == target:
                res[0] = self.firstloc(nums, target, m)
                res[1] = self.lastloc(nums, target, m)
                return res
            elif nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1
        return res
