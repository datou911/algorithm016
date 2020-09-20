# Created by Qin_young on 2020/9/20 21:22 
# coding = utf-8

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


# 前序遍历 ：先遍历父节点再到子节点
class Solution:
    def preorder(self, root):
        if not root: return
        res = [root.val]
        for node in root.children:
            res.extend(self.preorder(node))
        return res

