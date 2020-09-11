'''
链表逆序输出的方法：1、递归   2、栈

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''

#递归
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if head is None:
            return []
        res = self.reversePrint(head.next)
        res.append(head.val)
        return res

#堆栈
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack=[]
        while(head is not None):
            stack.append(head.val)
            head=head.next
        return stack[::-1]

