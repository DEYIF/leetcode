from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return
        # 定义三个指针
        left = 0           # 指向0区域的右边界
        curr = 0          # 当前正在处理的元素
        right = len(nums) - 1  # 指向2区域的左边界
        
        # 当curr指针还没有与right指针交叉时继续处理
        while curr <= right:
            if nums[curr] == 0:
                # 遇到0时，将其与left指针位置的数交换
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
            elif nums[curr] == 2:
                # 遇到2时，将其与right指针位置的数交换
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
                # 注意这里不移动curr，因为交换来的数还需要处理
            else:
                # 遇到1时，不需要交换，继续向前移动
                curr += 1

            # return nums

nums = [2,0,2,1,1,0]
solution = Solution()
print(solution.sortColors(nums))