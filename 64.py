class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def display(self):
        if not self.head:
            print("Linked List is empty")
            return
        else:
            temp = self.head
            print("The linked list is:", end=" ")
            while temp:
                print(temp.data, end=" ")
                temp = temp.next


l = LinkedList()
l.add(9)
l.add(18)
l.add(25)
l.display()