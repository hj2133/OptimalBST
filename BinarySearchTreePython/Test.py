###############################################################################################################################
#
# Template from Lab 4, COMP 251, Helana Jaraiseh
#
# This file was translated from Java into Python with ChatGPT. 
#
# Read through Python code and ran tests for BinarySearchTree class - passed all tests
#
###############################################################################################################################
# 
# References
# 
# [1] https://www.youtube.com/watch?v=_A9BXSpmeYI
#
###############################################################################################################################

import BinarySearchTree as BST # import as shown in source [1] 

def main():
        # Test with Base Cases
        # This tree should be empty

        # Create empty tree
        null_tree = BST.BinarySearchTree(None) # source [1]

        # Test size()
        print(null_tree.size())  # 0

        # Test height()
        print(null_tree.height())  # -1

        # Test preOrder()
        print(null_tree.list_pre_order())  # []

        # Test inOrder()
        print(null_tree.list_in_order())  # []

        # Test postOrder()
        print(null_tree.list_post_order())  # []

        # Test largest()
        print(null_tree.largest())  # None

        # Test smallest()
        print(null_tree.smallest())  # None

        # Test median()
        print(null_tree.median())  # None

        # This tree should now look like this:      [6]        , a single root

        # Test insert to empty tree
        null_tree.insert(6)
        print(null_tree.list_in_order())  # [6]

        # Space
        print("\n")

        # Test with Integer Tree
        # This tree should look like this:
        #
        #            [5]
        #           /   \
        #          /     \
        #        [1]    [35]
        #         \     /  \
        #         [3] [7] [100]
        #           \        \
        #           [4]     [102]
        #                   /
        #               [101]
        #
        #
        # Create binary search tree with one node (root)
        tree = BST.BinarySearchTree(5) # source [1]

        # Test insert(data)
        tree.insert(35)
        tree.insert(7)
        tree.insert(100)
        tree.insert(None)  # test None insert
        tree.insert(1)
        tree.insert(3)
        tree.insert(4)
        tree.insert(35)  # test duplicate
        tree.insert(102)
        tree.insert(101)

        # Test delete(data)
        tree.insert(103)
        tree.delete(103)

        # Test searchItem(data)
        tree.search_item(35)
        tree.search_item(9) # should not found

        # Test size()
        print(tree.size())  # 9

        # Test height()
        print(tree.height())  # 4

        # Test preOrder()
        print(tree.list_pre_order())  # [5, 1, 3, 4, 35, 7, 100, 102, 101]

        # Test inOrder()
        print(tree.list_in_order())  # [1, 3, 4, 5, 7, 35, 100, 101, 102]

        # Test postOrder()
        print(tree.list_post_order())  # [4, 3, 1, 7, 101, 102, 100, 35, 5]

        # Test largest()
        print(tree.largest())  # 102

        # Test smallest()
        print(tree.smallest())  # 1

        # Test median()
        print(tree.median())  # 7

        # Space
        print("\n")

        # Test with non-number Tree
        # This tree should look like this:
        #
        #            [Pizza]
        #            /     \
        #        [Cheese]  [Tea]
        #        /     \
        #       /       \
        #    [Apple]      [Pie]
        #       \         /
        #     [Bread] [Crepe]
        #          \
        #        [Cake]
        #
        #
        # Create binary search tree with one node (root)
        tree_s = BST.BinarySearchTree("Pizza") # source [1]

        # Test insert(data)
        tree_s.insert("Cheese")
        tree_s.insert("Cheese")  # test duplicate
        tree_s.insert("Apple")
        tree_s.insert("Bread")
        tree_s.insert(None)  # test None insert
        tree_s.insert("Pie")
        tree_s.insert("Cake")
        tree_s.insert("Tea")
        tree_s.insert("Crepe")

        # Test size()
        print(tree_s.size())  # 8

        # Test height()
        print(tree_s.height())  # 4

        # Test preOrder()
        print(tree_s.list_pre_order())  # ['Pizza', 'Cheese', 'Apple', 'Bread', 'Pie', 'Crepe', 'Tea']

        # Test inOrder()
        print(tree_s.list_in_order())  # ['Apple', 'Bread', 'Cake', 'Cheese', 'Crepe', 'Pie', 'Pizza', 'Tea']

        # Test postOrder()
        print(tree_s.list_post_order())  # ['Cake', 'Bread', 'Apple', 'Crepe', 'Pie', 'Cheese', 'Tea', 'Pizza']

        # Test largest()
        print(tree_s.largest())  # Tea

        # Test smallest()
        print(tree_s.smallest())  # Apple

        # Test median()
        print(tree_s.median())  # Cheese

# Run tests
main()
