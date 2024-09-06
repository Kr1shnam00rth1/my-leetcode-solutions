# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        while curr:
            t=curr.next
            curr.next=prev
            prev=curr
            if t:
                curr=t
            else:
                head=prev
                break
        return head
            
            s
