# Created by Qin_young on 2020/9/20 20:39 
# coding = utf-8


# Hash Table 时间复杂度为：O（n）
class Solution:
    def two_sum(self, nums, target):
        """用哈希表存储遍历过的数和它的index"""
        dct = {}
        for i, n in enumerate(nums):
            cp = target - n
            if cp in dct:
                return [dct[cp], i]
            else:
                dct[n] = i