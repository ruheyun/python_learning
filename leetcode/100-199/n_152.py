"""
152. 乘积最大子数组
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        f_max, f_min = 1, 1

        for x in nums:
            f_max, f_min = max(f_max * x, f_min * x, x), min(f_max * x, f_min * x, x)
            ans = max(ans, f_max)

        return ans