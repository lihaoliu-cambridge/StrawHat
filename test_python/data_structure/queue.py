class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


q = Queue()
print q.isEmpty()
q.enqueue('dog')
q.enqueue(4)
print q.isEmpty()
print q.dequeue()
print q.size()
print q.dequeue()
