class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    if head is None or head.next is None:
        return head
    rev_ll = None
    while head is not None:
        temp_ll = head.next
        head.next = rev_ll
        print("Head.next", head.next)
        rev_ll = head
        head = temp_ll
        print("\tHead", head)
    return rev_ll
