###############################################################################################################################
# 
# References
# 
# [1] https://stackoverflow.com/questions/20793082/java-comparing-generic-types
# 
# [2] https://www.youtube.com/watch?v=KNsg2qbOrjg
# 
# [3] https://www.youtube.com/watch?v=g_S5WuasWUE
# 
# [4] https://www.youtube.com/watch?v=MSPAezfDO9I
# 
# [5] Lectures - Week 6: BinaryTree.java, COMP 251, Opeyemi Adesina
#
# This file was translated from Java into Python with ChatGPT. 
#
# Read through Python code and tested it with test cases in Test.py - passed all tests.
#
##############################################################################################################################

import tkinter as tk;

class BinarySearchTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.parent = self.right = self.left = None

        def insert(self, new_leaf):
            if self.data > new_leaf.data: # insert is smaller than data; [1], [5]
                if self.left:
                    self.left.insert(new_leaf)
                else:
                    self.left = new_leaf
            elif self.data < new_leaf.data: # // insert is bigger than data; [1], [5]
                if self.right:
                    self.right.insert(new_leaf)
                else:
                    self.right = new_leaf
            else: # ignore duplicates
                print("ignored duplicate")
                return

        def delete(self, current_node, data):
            if current_node.left is None and current_node.right is None:
                if data == current_node.data:
                    current_node = None
                    return current_node
                else:
                    print("cannot delete non-existent item")
                    return current_node
            elif current_node.left is not None and current_node.right is None:
                if data == current_node.data:
                    return current_node.left
                else:
                    current_node.left = self.delete(current_node.left, data)
            elif current_node.left is None and current_node.right is not None:
                if data == current_node.data:
                    return current_node.right
                else:
                    current_node.right = self.delete(current_node.right, data)
            else:
                if data == current_node.data:
                    current_node.data = current_node.right.smallest()
                    current_node.right = self.delete(current_node.right, current_node.right.smallest())
                else:
                    if data > current_node.data:
                        current_node.right = self.delete(current_node.right, data)
                    else:
                        current_node.left = self.delete(current_node.left, data)
            return current_node

        def search_item(self, current_node, data):
            if data != current_node.data and current_node.left is None and current_node.right is None:
                print("could not find item")
            elif data < current_node.data:
                self.search_item(current_node.left, data)
            elif data > current_node.data:
                self.search_item(current_node.right, data)
            else:
                print("found item:", current_node.data)
                return current_node.data

        def height(self): # [5]
            if not self.left and not self.right:
                return 0
            elif self.left and not self.right:
                return self.left.height() + 1
            elif not self.left and self.right:
                return self.right.height() + 1
            else:
                return max(self.left.height(), self.right.height()) + 1

        def size(self): # [5]
            if not self.left and not self.right:
                return 1
            elif self.left and not self.right:
                return self.left.size() + 1
            elif not self.left and self.right:
                return self.right.size() + 1
            else:
                return self.left.size() + self.right.size() + 1

        def pre_order(self, elements): # [5]
            elements.append(self.data)
            if self.left:
                self.left.pre_order(elements)
            if self.right:
                self.right.pre_order(elements)

        def in_order(self, elements): # [3], [5]
            if self.left:
                self.left.in_order(elements)
            elements.append(self.data)
            if self.right:
                self.right.in_order(elements)

        def post_order(self, elements): # [5]
            if self.left:
                self.left.post_order(elements)
            if self.right:
                self.right.post_order(elements)
            elements.append(self.data)

        def largest(self):
            return self.right.largest() if self.right else self.data

        def smallest(self):
            return self.left.smallest() if self.left else self.data

        # Traverse tree, draw each node and its edges
        def drawNodeAndEdges(self, current_node, canvas, x0, y0, x1, y1):
            if not current_node.left and not current_node.right: # Draw node with no edges
                node = canvas.create_oval(x0, y0, x1, y1, fill = '#CCC', outline = 'grey')
                text = canvas.create_text(x0 + 25, y0 + 21, text = current_node.data, font = ('Georgia', 14))
                return
            elif current_node.left and not current_node.right: # Draw node with left edge
                edgeLeft = canvas.create_line(x0 + 7, y1 - 10, x0 - (2 ** current_node.height()) * 12.5, y1 + 65, width = 3, fill = '#666')
                node = canvas.create_oval(x0, y0, x1, y1, fill = '#CCC', outline = 'grey')
                text = canvas.create_text(x0 + 25, y0 + 21, text = current_node.data, font = ('Georgia', 14))
                self.drawNodeAndEdges(current_node.left, canvas, x0 - (2 ** current_node.height()) * 13.3, y0 + 90, x1 - (2 ** current_node.height()) * 13.3, y1 + 90) # traverse to left child
            elif not current_node.left and current_node.right: # Draw node with right edge
                edgeRight = canvas.create_line(x1 - 7, y1 - 10, x1 + (2 ** current_node.height()) * 12.5, y1 + 65, width = 3, fill = '#666')
                node = canvas.create_oval(x0, y0, x1, y1, fill = '#CCC', outline = 'grey')
                text = canvas.create_text(x0 + 25, y0 + 21, text = current_node.data, font = ('Georgia', 14))
                self.drawNodeAndEdges(current_node.right, canvas, x0 + (2 ** current_node.height()) * 13.3, y0 + 90, x1 + (2 ** current_node.height()) * 13.3, y1 + 90) # traverse to right child
            else: # Draw node with both left and right edges
                edgeLeft = canvas.create_line(x0 + 7, y1 - 10, x0 - (2 ** current_node.height()) * 12.5, y1 + 65, width = 3, fill = '#666')
                self.drawNodeAndEdges(current_node.left, canvas, x0 - (2 ** current_node.height()) * 13.3, y0 + 90, x1 - (2 ** current_node.height()) * 13.3, y1 + 90) # traverse to left child
                edgeRight = canvas.create_line(x1 - 7, y1 - 10, x1 + (2 ** current_node.height()) * 12.5, y1 + 65, width = 3, fill = '#666')
                self.drawNodeAndEdges(current_node.right, canvas, x0 + (2 ** current_node.height()) * 13.3, y0 + 90, x1 + (2 ** current_node.height()) * 13.3, y1 + 90) # traverse to right child
                node = canvas.create_oval(x0, y0, x1, y1, fill = '#CCC', outline = 'grey')
                text = canvas.create_text(x0 + 25, y0 + 21, text = current_node.data, font = ('Georgia', 14))

    def __init__(self, data):
        self.root = self.Node(data)
        self.elements = []

########################################### Print Tree Methods ############################################

    # Organizes the elements in their preorder fashion
    def list_pre_order(self):
        self.pre_order()
        temp = self.elements
        self.elements = []
        return temp
    
    # Organizes the elements in their inorder fashion
    def list_in_order(self):
        self.in_order()
        temp = self.elements
        self.elements = []
        return temp

    # Organizes the elements in their postorder fashion
    def list_post_order(self):
        self.post_order()
        temp = self.elements
        self.elements = []
        return temp

    # Organizes the elements in their inorder fashion
    def get_elements(self):
        self.in_order()
        temp = self.elements
        self.elements = []
        return temp

    def get_root(self):
        return self.root

    def is_empty(self):
        return self.root.data is None

    def __str__(self):
        return str(self.get_elements())

    def initialize(self, data):
        self.root = self.Node(data)

  ########################################### Modifiers ############################################

    # insert node to binary search tree; worst case: O(n); [5]
    def insert(self, data): 
        new_leaf = self.Node(data)
        if new_leaf.data is None: # ignore null inserts
            print("ignored null insert")
            return
        elif self.is_empty(): # base case: empty tree
            self.root = new_leaf
        else:
            self.root.insert(new_leaf)

    # delete node from binary search tree
    def delete(self, data):
        if self.is_empty():
            print("cannot delete item in empty tree")
        else:
            self.root.delete(self.root, data)

    # search node from binary search tree
    def search_item(self, data):
        if self.is_empty():
            print("cannot find item in empty tree")
        else:
            self.root.search_item(self.root, data)

    # find number of nodes in binary tree; base case: empty tree
    def size(self): 
        return 0 if self.is_empty() else self.root.size()

    # find height of binary tree; base case: empty tree
    def height(self): 
        return -1 if self.is_empty() else self.root.height()

    # list nodes in preOrder fashion; base case: empty tree
    def pre_order(self): 
        if not self.is_empty():
            self.root.pre_order(self.elements)

    # list nodes in inOrder fashion; base case: empty tree
    def in_order(self): 
        if not self.is_empty():
            self.root.in_order(self.elements)

    # list nodes in postOrder fashion; base case: empty tree
    def post_order(self): 
        if not self.is_empty():
            self.root.post_order(self.elements)

  ########################################### Accessors ############################################

    # find node with the largest data; base case: empty tree
    def largest(self): 
        return None if self.is_empty() else self.root.largest()

    # find node with the smallest data; base case: empty tree
    def smallest(self): 
        return None if self.is_empty() else self.root.smallest()

    # find middle node [4]; base case: empty tree
    def median(self): 
        if self.is_empty():
            return None
        temp = self.get_elements()
        if len(temp) % 2 == 0: # even number of nodes
            x = len(temp) - (len(temp) // 2) - 1
            return temp[x]
        else: # odd number of nodes
            y = ((len(temp) + 1) // 2) - 1
            return temp[y]

  ############################################## GUI ##############################################

    def gui(self):
        # Setup GUI
        root = tk.Tk()
        root.geometry('1500x550')
        root.title('Optimal BST Solution')

        # Setup Tree Canvas and Optimal BST Solution Box
        treeCanvasAndSolution = tk.Canvas(root, width = 1200, height = 550, bg = 'white')
        treeCanvasAndSolution.pack()
        treeCanvasAndSolution.create_rectangle((875, 0, 1500, 550), fill = '#99CCCC', outline = '#99CCCC')
        treeCanvasAndSolution.create_rectangle((0, 0, 875, 550), fill = 'white', outline = 'white')

        # Draw BST Tree
        if not self.is_empty():
            self.root.drawNodeAndEdges(self.root, treeCanvasAndSolution, 413, 50, 463, 100)
       
        # Run GUI
        root.mainloop()
