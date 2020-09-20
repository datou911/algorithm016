# Created by Qin_young on 2020/9/20 22:00 
# coding = utf-8

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root):
        if root is None:
            return []

        result = []
        previous_layer = [root]

        while previous_layer:
            current_layer = []
            result.append([])
            for node in previous_layer:
                result[-1].append(node.val)
                current_layer.extend(node.children)
            previous_layer = current_layer
        return result

