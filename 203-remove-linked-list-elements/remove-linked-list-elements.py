# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        while head and head.val==val:
            head=head.next
        prev=None
        cur=head
        while cur:
            if cur.val==val:
                prev.next=cur.next
            else:
                prev=cur
            cur=cur.next
        return head
            
        