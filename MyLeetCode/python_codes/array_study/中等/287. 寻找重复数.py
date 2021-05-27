"""
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。
假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。

示例 1：

输入：nums = [1,3,4,2,2]
输出：2
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dd = {}
        for i in nums:
            if i in dd:
                return i
            else:
                dd[i]= 1


if __name__ == '__main__':
    res = Solution().findDuplicate([1, 3, 4, 2, 2])
    print(res)
