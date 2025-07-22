"""
LeetCode Problem: 1019. next-greater-node-in-linked-list
Difficulty: M
Link: https://leetcode.cn/problems/next-greater-node-in-linked-list/description/

Author: VastEpiphany
Date: 2025-07-22

"""
from typing import List,Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values):
    """辅助函数：从数组创建链表"""
    if not values:
        return None
    
    head = ListNode(values[0])  # 创建头节点
    current = head
    
    # 逐个创建后续节点并连接
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def print_linked_list(head):
    """辅助函数：打印链表内容"""
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    print(values)

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        ans = []
        while head:
            while stack and head.val > stack[-1][0]:
                ans[stack.pop()[1]] = head.val
            stack.append((head.val,len(ans)))
            ans.append(0)
            head = head.next

        return ans

if __name__ == '__main__':
    sol = Solution()
    
        