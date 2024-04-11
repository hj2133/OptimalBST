###############################################################################################################################
# 
# Updated on April 10, 2024 at 10:23 pm - added probability text, sum of probabilities catch and big tree drawing catch
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
# [6] https://www.youtube.com/watch?v=CTUTPSXyBO8
#
# This file was translated from Java into Python with ChatGPT. 
#
# Read through Python code and tested it with test cases in Test.py - passed all tests.
#
##############################################################################################################################

import tkinter as tk;

class OptimalBinarySearchTree:
    class Node:
        # Construct Node
        def __init__(self, data):
            self.data = data
            self.parent = self.right = self.left = None

        # Traverse tree and find correct location to insert node
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

        # Traverse tree and find correct location to delete node
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

        # Traverse tree and find matching node
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

        # Traverse tree branch and increment 1 per node visit
        def height(self): # [5]
            if not self.left and not self.right:
                return 0
            elif self.left and not self.right:
                return self.left.height() + 1
            elif not self.left and self.right:
                return self.right.height() + 1
            else:
                return max(self.left.height(), self.right.height()) + 1

        # Traverse all tree branches and increment 1 per node visit
        def size(self): # [5]
            if not self.left and not self.right:
                return 1
            elif self.left and not self.right:
                return self.left.size() + 1
            elif not self.left and self.right:
                return self.right.size() + 1
            else:
                return self.left.size() + self.right.size() + 1

        # Traverse tree and create preorder list
        def pre_order(self, elements): # [5]
            elements.append(self.data)
            if self.left:
                self.left.pre_order(elements)
            if self.right:
                self.right.pre_order(elements)

        # Traverse tree and create inorder list
        def in_order(self, elements): # [3], [5]
            if self.left:
                self.left.in_order(elements)
            elements.append(self.data)
            if self.right:
                self.right.in_order(elements)

        # Traverse tree and create postorder list
        def post_order(self, elements): # [5]
            if self.left:
                self.left.post_order(elements)
            if self.right:
                self.right.post_order(elements)
            elements.append(self.data)

        # Find node with largest item
        def largest(self):
            return self.right.largest() if self.right else self.data

        # Find node with smallest item
        def smallest(self):
            return self.left.smallest() if self.left else self.data

        # Traverse tree, draw each node and its edges
        def drawNodeAndEdges(self, current_node, canvas, x0, y0, x1, y1):
            if not current_node.left and not current_node.right: # Draw node with no edges
                node = canvas.create_oval(x0, y0, x1, y1, fill = '#CCC', outline = 'grey')
                data = canvas.create_text(x0 + 25, y0 + 21, text = current_node.data, font = ('Georgia', 14))
                return
            elif current_node.left and not current_node.right: # Draw node with left edge
                edgeLeft = canvas.create_line(x0 + 7, y1 - 10, x0 - (2 ** current_node.height()) * 12.5, y1 + 65, width = 3, fill = '#666')
                node = canvas.create_oval(x0, y0, x1, y1, fill = '#CCC', outline = 'grey')
                data = canvas.create_text(x0 + 25, y0 + 21, text = current_node.data, font = ('Georgia', 14))
                # traverse to the left
                self.drawNodeAndEdges(current_node.left, canvas, x0 - (2 ** current_node.height()) * 13.3, y0 + 90, x1 - (2 ** current_node.height()) * 13.3, y1 + 90) # traverse to left child
            elif not current_node.left and current_node.right: # Draw node with right edge
                edgeRight = canvas.create_line(x1 - 7, y1 - 10, x1 + (2 ** current_node.height()) * 12.5, y1 + 65, width = 3, fill = '#666')
                node = canvas.create_oval(x0, y0, x1, y1, fill = '#CCC', outline = 'grey')
                data = canvas.create_text(x0 + 25, y0 + 21, text = current_node.data, font = ('Georgia', 14))
                # traverse to the right
                self.drawNodeAndEdges(current_node.right, canvas, x0 + (2 ** current_node.height()) * 13.3, y0 + 90, x1 + (2 ** current_node.height()) * 13.3, y1 + 90) # traverse to right child
            else: # Draw node with both left and right edges
                # Draw edge then traverse to children
                edgeLeft = canvas.create_line(x0 + 7, y1 - 10, x0 - (2 ** current_node.height()) * 12.5, y1 + 65, width = 3, fill = '#666')
                self.drawNodeAndEdges(current_node.left, canvas, x0 - (2 ** current_node.height()) * 13.3, y0 + 90, x1 - (2 ** current_node.height()) * 13.3, y1 + 90) # traverse to left child
                edgeRight = canvas.create_line(x1 - 7, y1 - 10, x1 + (2 ** current_node.height()) * 12.5, y1 + 65, width = 3, fill = '#666')
                self.drawNodeAndEdges(current_node.right, canvas, x0 + (2 ** current_node.height()) * 13.3, y0 + 90, x1 + (2 ** current_node.height()) * 13.3, y1 + 90) # traverse to right child
                # draw node
                node = canvas.create_oval(x0, y0, x1, y1, fill = '#CCC', outline = 'grey')
                data = canvas.create_text(x0 + 25, y0 + 21, text = current_node.data, font = ('Georgia', 14))

        # Traverse tree, draw each node, its edges and probabilities
        def drawNodeAndEdgesProb(self, current_node, p, keys, canvas, x0, y0, x1, y1):
            if not current_node.left and not current_node.right: # Draw node with no edges
                node = canvas.create_oval(x0, y0, x1, y1, fill = '#CCC', outline = 'grey')
                data = canvas.create_text(x0 + 25, y0 + 21, text = current_node.data, font = ('Georgia', 14))
                # Add probability text
                probIndex = keys.index(current_node.data)
                prob = canvas.create_text(x1 - 25, y1 + 7, text = "{:.2f}".format(p[probIndex]), font = ('Georgia', 11))
                return
            elif current_node.left and not current_node.right: # Draw node with left edge
                edgeLeft = canvas.create_line(x0 + 7, y1 - 10, x0 - (2 ** current_node.height()) * 12.5, y1 + 65, width = 3, fill = '#666')
                node = canvas.create_oval(x0, y0, x1, y1, fill = '#CCC', outline = 'grey')
                data = canvas.create_text(x0 + 25, y0 + 21, text = current_node.data, font = ('Georgia', 14))
                # Add probability text
                probIndex = keys.index(current_node.data)
                prob = canvas.create_text(x1 - 25, y1 + 7, text = "{:.2f}".format(p[probIndex]), font = ('Georgia', 11))
                # traverse to the left
                self.drawNodeAndEdgesProb(current_node.left, p, keys, canvas, x0 - (2 ** current_node.height()) * 13.3, y0 + 90, x1 - (2 ** current_node.height()) * 13.3, y1 + 90) # traverse to left child
            elif not current_node.left and current_node.right: # Draw node with right edge
                edgeRight = canvas.create_line(x1 - 7, y1 - 10, x1 + (2 ** current_node.height()) * 12.5, y1 + 65, width = 3, fill = '#666')
                node = canvas.create_oval(x0, y0, x1, y1, fill = '#CCC', outline = 'grey')
                data = canvas.create_text(x0 + 25, y0 + 21, text = current_node.data, font = ('Georgia', 14))
                # Add probability text
                probIndex = keys.index(current_node.data)
                prob = canvas.create_text(x1 - 25, y1 + 7, text = "{:.2f}".format(p[probIndex]), font = ('Georgia', 11))
                # traverse to the right
                self.drawNodeAndEdgesProb(current_node.right, p, keys, canvas, x0 + (2 ** current_node.height()) * 13.3, y0 + 90, x1 + (2 ** current_node.height()) * 13.3, y1 + 90) # traverse to right child
            else: # Draw node with both left and right edges
                # Draw edge then traverse to children
                edgeLeft = canvas.create_line(x0 + 7, y1 - 10, x0 - (2 ** current_node.height()) * 12.5, y1 + 65, width = 3, fill = '#666')
                self.drawNodeAndEdgesProb(current_node.left, p, keys, canvas, x0 - (2 ** current_node.height()) * 13.3, y0 + 90, x1 - (2 ** current_node.height()) * 13.3, y1 + 90) # traverse to left child
                edgeRight = canvas.create_line(x1 - 7, y1 - 10, x1 + (2 ** current_node.height()) * 12.5, y1 + 65, width = 3, fill = '#666')
                self.drawNodeAndEdgesProb(current_node.right, p, keys, canvas, x0 + (2 ** current_node.height()) * 13.3, y0 + 90, x1 + (2 ** current_node.height()) * 13.3, y1 + 90) # traverse to right child
                # draw node
                node = canvas.create_oval(x0, y0, x1, y1, fill = '#CCC', outline = 'grey')
                data = canvas.create_text(x0 + 25, y0 + 21, text = current_node.data, font = ('Georgia', 14))
                # Add probability text
                probIndex = keys.index(current_node.data)
                prob = canvas.create_text(x1 - 25, y1 + 7, text = "{:.2f}".format(p[probIndex]), font = ('Georgia', 11))

    # Constructor for binary search tree
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

    # Fetch root node
    def get_root(self):
        return self.root

    # Check if tree is empty
    def is_empty(self):
        return self.root.data is None

    # Print elements
    def __str__(self):
        return str(self.get_elements())

    # Initialize a root node
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

  ######################################## Optimal BST Functions ###################################
    
    # Creates the optimal bst from existing binary search tree; 
    # Used stack method in Reference [6] to read from root matrix and create tree
    def optimal_bst_create(self, keys, p, n):
        if round(sum(p), 2) != 1: # check probability sum is 1 (up to 2 decimals)
            print("please make sure the probabilities add up to 1")
            return self
        else:
            if self.is_empty():
                return self
            else:
                R = self.optimal_bst(keys, p, n)
                optimal_bst_build = OptimalBinarySearchTree(keys[R[1][n] - 1])
                # print(R[1][n]) - internal debug line
                # print(keys[R[1][n]]) - internal debug line
                stack = []
                stack.append([1, n])
                while(stack):
                    [i, j] = stack.pop()
                    l = R[i][j]
                    # print(R[i][j]) - internal debug line
                    if l < j:
                        optimal_bst_build.insert(keys[R[l + 1][j] - 1])
                        stack.append([l + 1, j])
                    if i < l:
                        optimal_bst_build.insert(keys[R[i][l - 1] - 1])
                        stack.append([i, l - 1])
            return optimal_bst_build

    # Finds the minimal cost, the cost matrix and returns the root matrix
    def optimal_bst(self, keys, p, n):
        if round(sum(p), 2) != 1: # check probability sum is 1 (up to 2 decimals)
            print("please make sure the probabilities add up to 1")
            return
        else: 
            cost = [[0 for _ in range(n+1)] for _ in range(n+2)]
            root = [[0 for _ in range(n+1)] for _ in range(n+2)]
            for i in range(1, n+1):
                cost[i][i] = p[i-1]
                root[i][i] = i
            for L in range(2, n+1):
                for i in range(1, n-L+2):
                    j = i+L-1
                    cost[i][j] = float('inf')
                    sum_p_ij = sum(p[i-1:j])  
                    for r in range(i, j+1):
                        c = ((cost[i][r-1] if r > i else 0) + (cost[r+1][j] if r < j else 0) + sum_p_ij)
                        if c < cost[i][j]:
                            cost[i][j] = c
                            root[i][j] = r
            cost[n+1] = [0 for _ in range(n+1)]
            root[n+1] = [0 for _ in range(n+1)]
            # print(cost[1][n]) - check precision (correct); value shouldn't be rounded when computing cost and finding roots        
            cost_print = cost[1:] # removes top row of 0's
            root_print = root[1:] # removes top row of 0's
            self.print_matrix(cost_print, "Cost Matrix:")
            print("\n")
            self.print_matrix(root_print, "Root Matrix:")
            print("\n")
            print("The minimal cost is: " + str(cost_print[0][n]))
            return root

    # Prints a matrix
    def print_matrix(self, mat, label):
        print(label)
        for row in mat:
            print(" ".join(f"{v:.2f}" if isinstance(v, float) else str(v) for v in row))

  ############################################## GUI ##############################################

    # Draws an Optimal BST (if the probability sum is 1; else, it draws a bst)
    def guiOptimal(self, p):
        # Screen Size Limit - Maximum Tree with 5 Levels
        if self.height() + 1 > 5: # cannot fit on screen
           print("tree cannot fit on screen")
           return
        else:
            # Setup GUI
            root = tk.Tk()
            root.geometry('1500x550')
            root.title('Optimal BST Solution')
            # Setup Tree Canvas and Optimal BST Solution Box
            treeCanvasAndSolution = tk.Canvas(root, width = 1500, height = 550, bg = 'white')
            treeCanvasAndSolution.pack()
            treeCanvasAndSolution.create_rectangle((0, 0, 200, 550), fill = '#99CCCC', outline = '#99CCCC')
            treeCanvasAndSolution.create_rectangle((1300, 0, 1500, 550), fill = '#99CCCC', outline = '#99CCCC')
            treeCanvasAndSolution.create_rectangle((200, 0, 1300, 550), fill = 'white', outline = 'white')
            # Draw BST Tree
            if not self.is_empty():
                if round(sum(p), 2) != 1: # draw bst
                    self.root.drawNodeAndEdges(self.root, treeCanvasAndSolution, 725, 50, 775, 100)
                else: # draw optimal bst
                    self.root.drawNodeAndEdgesProb(self.root, p, self.list_in_order(), treeCanvasAndSolution, 725, 50, 775, 100)
            # Run GUI
            root.mainloop()

    # Draws a BST
    def gui(self):
        # Screen Size Limit - Maximum Tree with 5 Levels
        if self.height() + 1 > 5: # cannot fit on screen
            print("tree cannot fit on screen")
            return
        else:
            # Setup GUI
            root = tk.Tk()
            root.geometry('1500x550')
            root.title('Optimal BST Solution')
            # Setup Tree Canvas and Optimal BST Solution Box
            treeCanvasAndSolution = tk.Canvas(root, width = 1500, height = 550, bg = 'white')
            treeCanvasAndSolution.pack()
            treeCanvasAndSolution.create_rectangle((0, 0, 200, 550), fill = '#99CCCC', outline = '#99CCCC')
            treeCanvasAndSolution.create_rectangle((1300, 0, 1500, 550), fill = '#99CCCC', outline = '#99CCCC')
            treeCanvasAndSolution.create_rectangle((200, 0, 1300, 550), fill = 'white', outline = 'white')
            # Draw BST Tree
            if not self.is_empty():
                self.root.drawNodeAndEdges(self.root, treeCanvasAndSolution, 725, 50, 775, 100)
            # Run GUI
            root.mainloop()
