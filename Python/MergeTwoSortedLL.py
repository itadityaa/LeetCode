class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    dummy_node = ListNode()
    tail_dummy_node = dummy_node

    while list1 and list2:
        if list1.val < list2.val:
            tail_dummy_node.next = list1
            list1 = list1.next
        else:
            tail_dummy_node.next = list2
            list2 = list2.next
        tail_dummy_node = tail_dummy_node.next

    if list1:
        tail_dummy_node.next = list1
    if list2:
        tail_dummy_node.next = list2

    return dummy_node.next
