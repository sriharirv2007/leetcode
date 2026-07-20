# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        x = None

        for i in lists:

            if x is None:
                x = i
                continue

            d = ListNode()
            current = d

            a = x
            b = i

            while a and b:
                if a.val <= b.val:
                    current.next = a
                    a = a.next
                else:
                    current.next = b
                    b = b.next

                current = current.next

            if a:
                current.next = a
            else:
                current.next = b

            x = d.next

        return x

        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        