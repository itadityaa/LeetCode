class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        end_iterator = self.head
        while end_iterator.next:
            end_iterator = end_iterator.next
        end_iterator.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        length_iterator = self.head
        while length_iterator:
            count += 1
            length_iterator = length_iterator.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        print(f"Removing from the index: {index}")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        remove_iterator = self.head
        while remove_iterator:
            if count == index - 1:
                remove_iterator.next = remove_iterator.next.next
                break
            remove_iterator = remove_iterator.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        print(f"Inserting at: {index}")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        insert_iterator = self.head
        while insert_iterator:
            if count == index - 1:
                node = Node(data, insert_iterator.next)
                insert_iterator.next = node
                break

            insert_iterator = insert_iterator.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        print(f"Inserting {data_to_insert} after {data_after}")

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        insert_after_iterator = self.head
        while insert_after_iterator:
            if insert_after_iterator.data == data_after:
                insert_after_iterator.next = Node(data_to_insert, insert_after_iterator.next)
                break

            insert_after_iterator = insert_after_iterator.next

    def remove_by_value(self, data_to_remove):
        if self.head is None:
            return

        print(f"Removing {data_to_remove}")
        if self.head.data == data_to_remove:
            self.head = self.head.next
            return

        remove_by_iterator = self.head
        while remove_by_iterator:
            if remove_by_iterator.next.data == data_to_remove:
                remove_by_iterator.next = remove_by_iterator.next.next
                break

            remove_by_iterator = remove_by_iterator.next

    def print(self):
        if self.head is None:
            print("Empty Linked List")
            return

        iterator = self.head
        while iterator:
            print(iterator.data)
            iterator = iterator.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.insert_at_beginning(25)
    llist.insert_at_beginning(24)
    llist.insert_at_end(26)
    llist.print()
    llist.remove_at(1)
    print("\nUpdate Linked List")
    llist.print()
    llist.insert_at(0, 23)
    llist.insert_at(2, 25)
    llist.insert_at(4, 27)
    llist.print()
    llist.insert_after_value(27, 28)
    llist.print()
    llist.remove_by_value(28)
    llist.print()
    print(f"Length: {llist.get_length()}")
