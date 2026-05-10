"""
215. 数组中的第K个最大元素
"""
from typing import List
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        时间复杂度：O(nlogn)    空间复杂度：O(1)
        """
        nums.sort()
        return nums[-k]
    
    def method(self, nums: List[int], k: int) -> int:
        """
        时间复杂度：O(n)    空间复杂度：O(n)
        """
        def quick_select(nums, k):
            pivot = random.choice(nums)
            big, equal, small = [], [], []
            for num in nums:
                if num > pivot:
                    big.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)
            if k <= len(big):
                return quick_select(big, k)
            elif k > len(nums) - len(small):
                return quick_select(small, k - len(nums) + len(small))
            else:
                return pivot
        
        return quick_select(nums, k)