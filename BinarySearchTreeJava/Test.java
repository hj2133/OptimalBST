/** Test file for BinarySearchTree from Lab 4, COMP 251, Helana Jaraiseh **/

public class Test 
{
	public static void main(String[] args) 
	{
		/////////////////////////////////////// Test with Base Cases //////////////////////////////////////////////
		// This tree should be empty
		
		// Create empty tree
		BinarySearchTree<Integer> nullTree = new BinarySearchTree<Integer>(null);
		
		// Test size()
		System.out.println(nullTree.size()); // 0
				
		// Test height()
		System.out.println(nullTree.height()); // -1

		// test delete()
		nullTree.delete(7); // error message
		
		// Test preOrder()
		System.out.println(nullTree.listPreOrder()); // []
				
		// Test inOrder()
		System.out.println(nullTree.listInOrder()); // []
				
		// Test postOrder()
		System.out.println(nullTree.listPostOrder()); // []
				
		// Test largest()
		System.out.println(nullTree.largest()); // null
				
		// Test smallest()
		System.out.println(nullTree.smallest()); // null
				
		// Test median()
		System.out.println(nullTree.median()); // null
		
		// This tree should now look like this:      [6]        , a single root
		
		// Test insert to empty tree
		nullTree.insert(6);
		System.out.println(nullTree.listInOrder()); // [6]
		
		// Space
		System.out.println("\n");
		
		
		
		/////////////////////////////////////// Test with Integer Tree //////////////////////////////////////////////
		
		/* This tree should look like this:
		 * 
		 * 			     [5]
		 * 			    /   \
		 * 			   /     \
		 * 		   [1]    [35]
		 * 		    \     /  \
		 *        [3] [7] [100]
		 *          \        \
		 *          [4]     [102]
		 *                   /
		 *                [101]
		 *            
		 * */
		
		
		// Create binary search tree with one node (root)
		BinarySearchTree<Integer> tree = new BinarySearchTree<Integer>(5);
		
		// Test insert(data)
		tree.insert(35);
		tree.insert(7);
		tree.insert(100);
		tree.insert(null); // test null insert
		tree.insert(1);
		tree.insert(3);
		tree.insert(4);
		tree.insert(35); // test duplicate
		tree.insert(102);
		tree.insert(101);

		// Test delete(data)
		tree.insert(103); // insert leaf node
		System.out.println(tree.listPreOrder()); // [5, 1, 3, 4, 35, 7, 100, 102, 101, 103]
		tree.delete(103); // delete leaf node
		System.out.println(tree.listPreOrder()); // [5, 1, 3, 4, 35, 7, 100, 102, 101]
		
		// test searchItem(data)
		tree.searchItem(35);
		tree.searchItem(9); // should not be found
		
		// Test size()
		System.out.println(tree.size()); // 9
		
		// Test height()
		System.out.println(tree.height()); // 4
		
		// Test preOrder()
		System.out.println(tree.listPreOrder()); // [5, 1, 3, 4, 35, 7, 100, 102, 101]
		
		// Test inOrder()
		System.out.println(tree.listInOrder()); // [1, 3, 4, 5, 7, 35, 100, 101, 102]
		
		// Test postOrder()
		System.out.println(tree.listPostOrder()); // [4, 3, 1, 7, 101, 102, 100, 35, 5]
		
		// Test largest()
		System.out.println(tree.largest()); // 102
		
		// Test smallest()
		System.out.println(tree.smallest()); // 1
		
		// Test median()
		System.out.println(tree.median()); // 7
		
		// Space
		System.out.println("\n");
		
		
		
		/////////////////////////////////////// Test with non-number Tree //////////////////////////////////////////////
		
		/* This tree should look like this:
		 * 
		 * 			     [Pizza]
		 * 			     /     \
		 * 		   [Cheese]  [Tea]
		 * 		    /     \
		 *       /       \
		 *      /         \
		 *  [Apple]      [Pie]
		 *      \         /
		 *    [Bread] [Crepe]
		 *        \
		 *       [Cake]
		 *            
		 * */
		
		// Create binary search tree with one node (root)
		BinarySearchTree<String> treeS = new BinarySearchTree<String>("Pizza");
				
		// Test insert(data)
		treeS.insert("Cheese");
		treeS.insert("Cheese"); // test duplicate
		treeS.insert("Apple");
		treeS.insert("Bread");
		treeS.insert(null); // test null insert
		treeS.insert("Pie");
		treeS.insert("Cake");
		treeS.insert("Tea");
		treeS.insert("Crepe");
				
		// Test size()
		System.out.println(treeS.size()); // 8
				
		// Test height()
		System.out.println(treeS.height()); // 4
				
		// Test preOrder()
		System.out.println(treeS.listPreOrder()); // [Pizza, Cheese, Apple, Bread, Pie, Crepe, Tea]
				
		// Test inOrder()
		System.out.println(treeS.listInOrder()); // [Apple, Bread, Cake, Cheese, Crepe, Pie, Pizza, Tea]
				
		// Test postOrder()
		System.out.println(treeS.listPostOrder()); // [Cake, Bread, Apple, Crepe, Pie, Cheese, Tea, Pizza]
				
		// Test largest()
		System.out.println(treeS.largest()); // Tea
				
		// Test smallest()
		System.out.println(treeS.smallest()); // Apple
				
		// Test median()
		System.out.println(treeS.median()); // Cheese
	}
}
