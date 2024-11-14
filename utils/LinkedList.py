class ListNode:

    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt


class LinkedList:

    def __init__(self):
        self.head = None

    def length(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def insert_at_first(self, val):
        if self.head:
            node = ListNode(val, self.head)
        else:
            node = ListNode(val)

        self.head = node

    def insert_at_last(self, val):

        if self.head is None:
            self.head = ListNode(val)
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = ListNode(val)

    def insert_at(self, index, val):
        if index < 0 or index > self.length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_first(val)
            return

        count = 1
        cur = self.head
        while cur:
            if count == index:
                node = ListNode(val)
                node.next = cur.next
                cur.next = node
                return
            cur = cur.next
            count += 1

    def insert_list(self, ll_list):
        self.head = None
        for i in ll_list:
            self.insert_at_last(i)

    def print(self):
        cur = self.head
        llstr = ""
        while cur:
            llstr += f"{cur.val}-->"
            cur = cur.next
        print(llstr)


if __name__ == "__main__":

    ll = LinkedList()
    ll.insert_list([1, 2, 3, 4, 5])
    ll.print()
    ll.insert_at(5, 40)
    ll.print()
