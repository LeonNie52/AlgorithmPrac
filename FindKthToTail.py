# -*- coding:utf-8 -*-
"""
输入一个链表，输出该链表中倒数第k个结点。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head:
            return head
        j = 0
        headj=head
        while j!=k-1:
            if headj.next:
                headj=headj.next
            else:
                return headj.next
            j +=1
            
        while headj.next:
            head=head.next
            headj=headj.next
        return head
            