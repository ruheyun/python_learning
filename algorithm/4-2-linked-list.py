
# Linked list class
class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode | None = None


# Initialize linked list
n0 = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(3)
n3 = ListNode(4)
n4 = ListNode(5)

n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4


# Insert node 
def insert(n0: ListNode, p: ListNode):
    n1 = n0.next
    n0.next = p
    p.next = n1


# Remove node
def remove(n0: ListNode):
    if not n0.next:
        return
    
    p = n0.next
    n1 = p.next
    n0.next = n1
        