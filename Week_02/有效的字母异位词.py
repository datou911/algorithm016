# Created by Qin_young on 2020/9/20 20:10 
# coding = utf-8
import collections


# 排序法：总体时间复杂度为 O(n log n)
class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# Hash Table 利用python内置模块
class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)


# 利用set去重的特性, 时间复杂度为O（logn）
# 性能比前面的都要好
class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        se = set(s)
        if se == set(t):
            for i in se:
                # 直接比较字符元素个数比较字符的个数
                if s.count(i) != t.count(i):
                    return False
            return True
        else:
            return False


