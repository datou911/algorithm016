# Created by Qin_young on 2020/9/20 22:08 
# coding = utf-8
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k: int):
        return [i[0] for i in Counter(nums).most_common(k)]