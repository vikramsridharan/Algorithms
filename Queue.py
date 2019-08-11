class Queue:

    def __init__(self):
        self.root = None

    def end_of_queue(self, item):
        if item.next == None:
            return item
        else:
            return self.end_of_queue(item.next)


    def queue(self, value):
        if self.root == None:
            self.root = Item(value, None)
        else:
            item = Item(value, None)
            end = self.end_of_queue(self.root)
            end.next = item

    def dequeue(self):
        if self.root != None:
            v = self.root.value
            if self.root.next != None:
                self.root = self.root.next
                return v
            else:
                self.root = None
                return v
        else:
            print("Error: queue is empty")
            return None



class Item:
    def __init__(self, value, next_item):
        self.value = value
        self.next = next_item

q = Queue()
q.queue(1)
q.queue(2)
q.queue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())