from unsorted_single_linked_list import List

class Stack:
    def __init__(self):
        self.list = List()

    def push(self, item):
        self.list.add(item)

    def pop(self):
        root = self.list.root
        next = self.list.root.next
        self.list.root = next
        return root.value

    def is_empty(self):
        return True if self.list.root == None else False