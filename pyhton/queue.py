class queue:
    def __init__(self):
        self.queue=list()
    def add_element(self,num):
        if num not in self.queue:
            self.queue.insert(0,num)
        return True
        return False
    def size(self):
        return len(self.queue)
    def delete(self):
        if len(self.queue)>0:
            return self.queue.pop(0)
    def show(self):
        for i in self.queue:
            return i
            
abc=queue()
abc.add_element("one")
abc.add_element("two")
abc.add_element("three")
abc.add_element("four")
abc.delete()
abc.show()
print("the length of queue is ",abc.size())

            
