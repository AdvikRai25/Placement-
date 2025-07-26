class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newnode = Node(data)
        if self.root == None:
            self.root = newnode
        else:
            temp = self.root
            while True:
                if data < temp.data:
                    if temp.left == None:
                        temp.left = newnode
                        break
                    else:
                        temp = temp.left
                else:
                    if temp.right == None:
                        temp.right = newnode
                        break
                    else:
                        temp = temp.right

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)


t = Tree()
t.insert(2)
t.insert(3)
t.insert(4)
t.insert(5)
t.insert(7)
t.insert(12)
t.insert(50)
t.insert(75)
t.insert(100)
t.insert(107)
t.insert(110)
t.insert(116)
t.insert(117)

print("Inorder traversal:")
t.inorder(t.root)

print("Preorder traversal:")
t.preorder(t.root)

print("Postorder traversal:")
t.postorder(t.root)