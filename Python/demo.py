# text = [1,2,3,4,5,6]
# new = iter(text)
# print(next(new))
# print(next(new))
# print(next(new))


class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class linked_list:
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            node = self.head
            while node is not None:
                print(node.data)
                node = node.ref
    
    def insert(self,data):
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
    
    def after(self,data,x):
        if self.head is None:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
        elif self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
        else:
            node = self.head
            while node is not None:
                if node.data == x:
                    break
                node = node.ref
            if node is None:
                print("Value not found")
            else: 
                new_node = Node(data)
                new_node.ref = node.ref
                node.ref = new_node

data =  linked_list()

data.insert(10)
data.insert(20)
data.after(100,20)
data.display()