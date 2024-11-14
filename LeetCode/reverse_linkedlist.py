from utils.LinkedList import LinkedList, ListNode
from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # if list1 is None:
        #     return list2
        #
        # if list2 is None:
        #     return list1
        #
        # if list2.val >= list1.val:
        #     list1.next = self.mergeTwoLists(list1.next, list2)
        #     return list1
        # else:
        #     list2.next = self.mergeTwoLists(list1, list2.next)
        #     return list2

        node = dummy = ListNode(0)
        
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next

        dummy.next = list1 or list2

        return node.next


if __name__ == "__main__":

    ll1 = LinkedList()
    ll1.insert_list([1, 2, 4])

    ll2 = LinkedList()
    ll2.insert_list([1, 3, 5])

    ll1.print()
    ll2.print()

    solution = Solution()
    s = solution.mergeTwoLists(ll1.head, ll2.head)

    while s:
        print(str(s.val), end="-->")
        s = s.next

