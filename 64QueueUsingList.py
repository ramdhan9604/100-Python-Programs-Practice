class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,value):
        self.items.insert(0,value)
    
    def dequeue(self):
        if self.items:
            return self.items.pop()
        return None
    
    def is_empty(self):
        return self.items==[]


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("Dequeued element: ",q.dequeue())
print("Queue is empty: ",q.is_empty())