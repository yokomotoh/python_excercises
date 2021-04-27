
class Node:
    def __init__(self, insertElm):
            self.left = None
            self.right = None
            self.val = insertElm

    def inorder(self):
        if not self:
            return
        if self.left:
            self.left.inorder()
        print(self.val, end=" ")
        if (self.right):
            self.right.inorder()


    def insert(self, insertElem):
        if not self:
            # print("insert", insertElem)
            self = Node(insertElem)
            return

        if (insertElem < self.val):
            # print(insertElem, self.val)
            if self.left :
                self.left.insert(insertElem)
            else:
                self.left = Node(insertElem)

        elif (self.val < insertElem):
            # print(self.val, insertElem)
            if self.right :
                self.right.insert(insertElem)
            else:
                self.right = Node(insertElem)

        else:
            print(self.val, insertElem)
            self.val = insertElem

    def search(self, searchElem):
        if self is None or self.val == searchElem:
            return self
        if self.val < searchElem:
            if self.right:
                return self.right.search(searchElem)
        if self.left :
            return self.left.search(searchElem)

if __name__ == '__main__':
    root = Node(10)
    '''
    root.left = Node(9)
    root.left.left = Node(7)
    root.right = Node(11)
    root.right.left = Node(8)
    root.right.right = Node(15)
    '''

    root.inorder()
    print("")

    insElm = 12
    root.insert(insElm)

    root.inorder()
    print("")

    root.insert(7)
    root.insert(8)
    root.insert(4)
    root.insert(11)

    root.inorder()
    print("")

    searchElm = 11
    if root.search(searchElm) is None :
        print("not found: ", searchElm)
    else:
        print("found: ", searchElm)