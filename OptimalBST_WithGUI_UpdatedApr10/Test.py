###############################################################################################################################
# 
# References
# 
# [1] https://www.youtube.com/watch?v=_A9BXSpmeYI
#
###############################################################################################################################

import OptimalBinarySearchTree as OptimalBST # import as shown in source [1] 

def main():
      
      # Test Optimal BST and GUI
      
      # level 0 (root); source [1]
      tree = OptimalBST.OptimalBinarySearchTree(35)

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
      # tree.insert(14)
      tree.insert(19)
      tree.insert(21)
      # tree.insert(29)
      tree.insert(32)
      tree.insert(47)
      # tree.insert(65)
      tree.insert(79)
      # tree.insert(93)
      tree.insert(104)
      tree.insert(117)
      tree.insert(124)
      tree.insert(136)

      # Create Probability List
      p = [0.02, 0.05, 0.03, 0.04, 0.05,
           0.01, 0.05, 0.03, 0.04, 0.05,
           0.01, 0.02, 0.07, 0.04, 0.05,
           0.03, 0.04, 0.03, 0.04, 0.05,
           0.03, 0.03, 0.03, 0.04, 0.05,
           0.05, 0.02]

      # for i in range(0, tree.size()):
        # p.append(1/tree.size())
    
      print("Sum of probabilities is:")
      print(round(sum(p), 2))

      print("\n")
      print("The tree (in order) has these probabilities:")
      print(tree.list_in_order())
      print(p) # check contents of probability list
      print("\n")

      # Test Optimal BST Creation
      tree = tree.optimal_bst_create(tree.list_in_order(), p, tree.size())
      
      # Draw Optimal BST
      tree.guiOptimal(p)

# Run tests
main()
