###############################################################################################################################
# 
# References
# 
# [1] https://www.youtube.com/watch?v=_A9BXSpmeYI
#
###############################################################################################################################

import BinarySearchTree as BST # import as shown in source [1] 

def main():
      # Create perfect binary tree (5 levels deep)
     
      # level 0 (root); source [1]
      tree = BST.BinarySearchTree(35)

      # level 1
      tree.insert(17) 
      tree.insert(100)

      # level 2
      tree.insert(10)
      tree.insert(25)
      tree.insert(73)
      tree.insert(120)

      # level 3
      tree.insert(5)
      tree.insert(13)
      tree.insert(20)
      tree.insert(30)
      tree.insert(51)
      tree.insert(86)
      tree.insert(111)
      tree.insert(131)

      # level 4
      tree.insert(1)
      tree.insert(7)
      tree.insert(11)
      tree.insert(14)
      tree.insert(19)
      tree.insert(21)
      tree.insert(29)
      tree.insert(32)
      tree.insert(47)
      tree.insert(65)
      tree.insert(79)
      tree.insert(93)
      tree.insert(104)
      tree.insert(117)
      tree.insert(124)
      tree.insert(136)

      # Break 
      tree.insert(None)  # test None insert
      tree.insert(35)  # test duplicate

      # Test GUI
      tree.gui()
      

# Run tests
main()
