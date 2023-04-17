class RBNode:
    def __init__(self, val):
        self.parent = None
        self.left = None
        self.right = None
        self.val = val
        self.color = False  # black false - red true


class RBTree:
    def __init__(self):
        self.nil = RBNode(0)
        self.nil.color = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil
        self.size = 0

    def search(self, value):  # returns false if not found and true if found
        current = self.root  # start search from tree root
        while current is not None:  # loop until the current node is none, or we found the word
            if str(value) == str(current.val):  # if value searched for is equal to the current node value
                return True  # word is found and we return true.
            elif str(value) < str(current.val):  # if it isn't found and value is smaller than current value
                current = current.left  # then continue in left side of tree
            else:
                current = current.right  # else continue on right side of tree
        return False

    def insert(self, val):
        # Ordinary Binary Search Insertion
        self.size += 1
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.color = True  # new node must be red

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                self.size -= 1  # since we didn't actually insert and word was already found in the tree
                print("ERROR: Word already in the dictionary!")
                return

        # Set the parent and insert the new node
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        # Fix the tree
        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.color:  # while the new node isn't the root and has color red
            if new_node.parent == new_node.parent.parent.right:  # if parent is right child of grandparent
                u = new_node.parent.parent.left  # uncle is the left child of the grandparent
                if u.color:  # if uncle is red then make him and parent black then make grandparent red
                    u.color = False
                    new_node.parent.color = False
                    new_node.parent.parent.color = True
                    new_node = new_node.parent.parent
                else:  # if uncle is black and new node the left node of its parent
                    if new_node == new_node.parent.left:  # if new node is left child we rotate right
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.color = False  # make parent black and grandparent red then rotate left
                    new_node.parent.parent.color = True
                    self.rotate_left(new_node.parent.parent)
            else:
                u = new_node.parent.parent.right  # parent is left child and uncle is right child

                if u.color:  # if uncle is red make uncle and parent black and grandparent red
                    u.color = False
                    new_node.parent.color = False
                    new_node.parent.parent.color = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:  # if new node is right of the parent rotate left
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.color = False  # make parent black and grandparent red then right rotate
                    new_node.parent.parent.color = True
                    self.rotate_right(new_node.parent.parent)
        self.root.color = False  # in the end make sure root is black

    # rotate left at node x
    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # rotate right at node x
    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def height(self, x):
        if x is None:
            return -2  # since we only want to count number of edges and not nodes
        else:
            return 1 + max(self.height(x.left), self.height(x.right))


def load_dict(tree):
    with open('EN-US-Dictionary.txt', 'r') as file:
        for line in file:
            tree.insert(line.strip('\n'))
    print("tree height is {}".format(tree.height(tree.root)))
    print("the new tree size is {} ".format(tree.size))
    return


def main():
    print("HI")
    tree = RBTree()
    while True:
        print("enter 1: to load dictionary\nenter 2: to insert new word\nenter 3: to search for existing word")
        print("enter 4: to print tree height\nenter 5: to print tree size\nenter anything else: to exit program")
        x = int(input())
        if x == 1:
            load_dict(tree)
        elif x == 2:
            word = input("enter word to insert\n")
            tree.insert(word)
            print("the new tree height is {}".format(tree.height(tree.root)))
            print("the new tree size is {} ".format(tree.size))
        elif x == 3:
            word = input("enter word to search for\n")
            if tree.search(word):
                print("found word")
            else:
                print("word not found")
        elif x == 4:
            print("tree height is {}".format(tree.height(tree.root)))
        elif x == 5:
            print("tree size is {} ".format(tree.size))
        else:
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
