class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, h, d):
        n = Node(d)
        # print("Start => head = ", h, ", data = ", d, ", Node = ", n)

        if h is None:
            h = n
            # print("first time, inserted =", n, h)
            return h

        if h.next is None:
            h.next = n
            # print("second time, head =", n, h.next)
            return h

        prev = h
        current = h.next
        while current:
            prev = current
            current = current.next

        prev.next = n
        # current = n
        # print("prev = ", prev, "current =", current, "prev.next ", prev.next)
        return h


if __name__ == '__main__':
    mylist = Solution()
    T = int(input())
    head = None
    for i in range(T):
        data = int(input())
        head = mylist.insert(head, data)
    mylist.display(head)
