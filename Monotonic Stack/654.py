"""
LeetCode Problem: 654. maximum-binary-tree
Difficulty: M
Link: https://leetcode.cn/problems/maximum-binary-tree/description/

Author: VastEpiphany
Date: 2025-07-22

"""

from typing import List,Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def BTree(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            best = left # 初始化一个best变量参数
            for i in range(left+1,right+1):
                if nums[i] > nums[best]:
                    best = i
            
            node = TreeNode(nums[best])
            node.left = BTree(left,best-1)
            node.right = BTree(best+1,right)

            return node
        return BTree(0,len(nums)-1)