class linkedlist:
    def __init__(self,value):
        self.node = value
        self.next = None




first = linkedlist(1)
second = linkedlist(2)
first.next = second

print(first.next.node)

  

    







