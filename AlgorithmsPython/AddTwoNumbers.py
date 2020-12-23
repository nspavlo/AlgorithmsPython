class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "<ListNode value:%s next:\n |%s>" % (self.val, self.next)

class LinkedList:
    def __init__(self):    
        self.head = None
        self.tail = None
        return

    def append(self, item):   
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        trace = LinkedList()

        while True:
            # value (12)
            val = l1.val + l2.val + carry

            # value (2) and carry (1)
            if val >= 10:
                val = val % 10
                carry = 1
            else:
                carry = 0

            # append
            trace.append(ListNode(val)) 

            # break if no more nodes to work with
            if not l1.next and not l2.next and carry == 0:
                break

            # create empty node if needed
            l1 = l1.next if l1.next else ListNode()
            l2 = l2.next if l2.next else ListNode()
                

        return trace.head


# given
l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
l2 = ListNode(9, ListNode(9, ListNode(9)))

# debug 
print(Solution().addTwoNumbers(l1, l2))