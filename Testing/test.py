import typing import Optional
# import typing import List
#
# def to_int(list1: Optional[ListNode]):
#     return int(s)
#
#
# def mergeTwoLists(list1: Optional[List], list2: Optional[List]) -> Optional[List]:
#     #
#
# def leetcode():
#     l1 = [1,3,4]
#     l2 = [6,3,7]
#
#     if mergeTwoLists(l1, l2) == [1,3,3,4,6,7]:
#         return True


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


ln = ListNode(1, ListNode(2, ListNode(3)))
print(ln.val)
print(ln.next.next.val)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = list1.append(list2)
        list1.sort()
        return(list1)

