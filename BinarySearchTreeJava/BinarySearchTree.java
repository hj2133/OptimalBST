/**
 * Used BinarySearchTree class from COMP 251, Lab 4 - Helana Jaraiseh as template
 * 
 * References
 * 
 * [1] 	"Java comparing generic types." StackOverflow.com, answered by Sotirios Delimanolis on Dec. 27, 2013, edited on Mar. 19, 2019. 
 * 	https://stackoverflow.com/questions/20793082/java-comparing-generic-types
 * 
 * [2] 	Blue Tree Code. "Algorithms: Binary Search Tree - Recursive Search and Insert." YouTube, Jul. 17, 2019. [Video].
 *	https://www.youtube.com/watch?v=KNsg2qbOrjg
 * 
 * [3] 	NeetCode. "Iterative & Recursive - Binary Tree Inorder Traversal - Leetcode 94 - Python." YouTube, Mar. 12, 2022. [Video].
 *	https://www.youtube.com/watch?v=g_S5WuasWUE
 * 
 * [4] 	FavTutor. "Find Median of BST | Binary Search Tree | FavTutor." YouTube, Feb 18, 2022. [Video].
 *	https://www.youtube.com/watch?v=MSPAezfDO9I
 * 
 * [5] 	Adesina, Opeyemi. "Lectures - Week 6: BinaryTree.java." Blackboard, COMP 251, June 2023. 
 * 
 * [6] 	mycodeschool. "Delete a node from Binary Search Tree." YouTube, May 1, 2014. [Video].
 *	https://www.youtube.com/watch?v=gcULXE7ViZw
 *
 **/

import java.util.*;

public class BinarySearchTree<T extends Comparable<? super T>> 
{	
	public class Node<T extends Comparable<? super T>> 
	{
		private T data;
		private Node<T> parent, right, left;
		
		public Node( T data ) 
		{
			this.data = data;
			parent = left = right = null;
		}
		
		private void insert(Node<T> currentNode, Node<T> newLeaf) // [2]
		{
			if(currentNode == null)
			{
				return;
			}
			
			else
			{
				if(currentNode.data.compareTo(newLeaf.data) > 0) // insert is smaller than data; [1], [5] 
				{
					if(currentNode.left != null)
					{
						insert(currentNode.left, newLeaf);
					}
					
					else
					{
						currentNode.left = newLeaf;
					}
				}
				
				else if(currentNode.data.compareTo(newLeaf.data) < 0) // insert is bigger than data; [1], [5]
				{
					if(currentNode.right != null)
					{
						insert(currentNode.right, newLeaf);
					}
					
					else
					{
						currentNode.right = newLeaf;
					}
				}
				
				else // ignore duplicates
				{
					System.out.println("ignored duplicate");
					return;
				}
			}
		}
		
		private Node<T> delete(Node<T> currentNode, T data) // [6] 
		{
			if(currentNode.left == null && currentNode.right == null) // case 1: node with no children
			{
				if(data.compareTo(currentNode.data) == 0)
				{
					currentNode = null;
					return currentNode;
				}
				
				else // made it to a leaf node without finding item
				{
					System.out.println("cannot delete non-existent item"); 
					return currentNode;
				}
			}
			
			else if(currentNode.left != null && currentNode.right == null) // case 2: node with left child
			{
				if(data.compareTo(currentNode.data) == 0)
				{
					return currentNode.left;
				}
				
				else
				{
					currentNode.left = delete(currentNode.left, data);
				}
			}
			
			else if(currentNode.left == null && currentNode.right != null) // case 3: node with right child
			{
				if(data.compareTo(currentNode.data) == 0)
				{
					return currentNode.right;
				}
				
				else
				{
					currentNode.right = delete(currentNode.right, data);
				}
			}
			
			else // case 4: node with two children
			{
				if(data.compareTo(currentNode.data) == 0)
				{
					currentNode.data = currentNode.right.smallest();
					currentNode.right = delete(currentNode.right, currentNode.right.smallest());
				}
				
				else
				{
					if(data.compareTo(currentNode.data) > 0)
					{
						currentNode.right = delete(currentNode.right, data);
					}
					
					else
					{
						currentNode.left = delete(currentNode.left, data);
					}
				}
			}
			
			return currentNode;
		}
		
		// finds an item in the tree
		private T searchItem(Node<T> currentNode, T data)
		{
			if(data.compareTo(currentNode.data) != 0 && currentNode.left == null && currentNode.right == null) // could not find item
			{
				System.out.println("could not find item");
			}
			
			else if(data.compareTo(currentNode.data) < 0) // move left
			{
				searchItem(currentNode.left, data);
			}
			
			else if(data.compareTo(currentNode.data) > 0) // move right
			{
				searchItem(currentNode.right, data);
			}
			
			else // found item
			{
				System.out.println("found item: " + currentNode.data); 
				return currentNode.data; 
			}
			
			return null;
		}
		
		//////////////////////////////////////////////////////////////////////////////////////////
		
		private int height(Node<T> node) // [5]
		{	
			if(node == null) // empty node
			{
				return 0;
			}
			
			else if(node.left == null && node.right == null) // node with no children
			{
				return 1;
			}
			
			else if(node.left != null && node.right == null) // node with left child
			{
				return height(node.left) + 1;
			}
			
			else if(node.left == null && node.right != null) // node with right child
			{
				return height(node.right) + 1;
			}
			
			else // node with two children
			{
				return Math.max(height(node.left), height(node.right)) + 1;
			}
		}
		
		private int size() // [5]
		{
			if(left == null && right == null) // node with no children
			{
				return 1;
			}
			
			else if(left != null && right == null) // node with left child
			{
				return left.size() + 1;
			}
			
			else if(left == null && right != null) // node with right child
			{
				return right.size() + 1;
			}
			
			else // node with two children
			{
				return left.size() + right.size() + 1;
			}
		}
		
		private void preOrder(List<T> elements) // [5]
		{
			elements.add(data);
			
			if(left != null)
			{
				left.preOrder(elements);
			}
			
			if(right != null)
			{
				right.preOrder(elements);
			}
		}
		
		private void inOrder(List<T> elements) // [3], [5]
		{
			if(left != null)
			{
				left.inOrder(elements);
			}
			
			elements.add(data);
			
			if(right != null)
			{
				right.inOrder(elements);
			}
		}
		
		private void postOrder(List<T> elements) // [5]
		{
			if(left != null)
			{
				left.postOrder(elements);
			}
			
			if(right != null)
			{
				right.postOrder(elements);
			}
			
			elements.add(data);
		}
		
		private T largest()
		{
			if(right != null)
			{
				return right.largest();
			}
			
			else 
			{
				return data;
			}
		}
		
		private T smallest()
		{
			if(left != null)
			{
				return left.smallest();
			}
			
			else 
			{
				return data;
			}
		}
	}
	
	private Node<T> root;
	List<T> elements;
	
	//default constructor
	public BinarySearchTree( T data ) 
	{
		root = new Node<T>( data );
		elements = new ArrayList<T>();
	}
	
	///////////////////////////////////////// Methods //////////////////////////////////////////
	
	//Organizes the elements in their preorder fashion
	public List<T> listPreOrder() 
	{ 
		preOrder();
		List<T> temp = elements;
		elements = new ArrayList<T>();
		return temp; 
	}
		
	//Organizes the elements in their inorder fashion
	public List<T> listInOrder() 
	{ 
		inOrder();
		List<T> temp = elements;
		elements = new ArrayList<T>();
		return temp; 
	}
		
	//Organizes the elements in their postorder fashion
	public List<T> listPostOrder() 
	{ 
		postOrder();
		List<T> temp = elements;
		elements = new ArrayList<T>();
		return temp; 
	}
		
	//Organizes the elements in their inorder fashion
	public List<T> getElements() 
	{ 
		inOrder();
		List<T> temp = elements;
		elements = new ArrayList<T>();
		return temp; 
	}
		
	public Node<T> getRoot() { return root; }
	
	public boolean isEmpty() { return root.data == null; }
		
	public String toString() { return getElements().toString(); }
		
	public void initialize( T data ) { root = new Node<T>( data ); }
	
	///////////////////////////////////////// Modifiers ////////////////////////////////////////
	
	// insert node to binary search tree
	public void insert( T data )
	{
		Node<T> newLeaf = new Node<T>(data);
		
		if(newLeaf.data == null) // ignore null inserts
		{
			System.out.println("ignored null insert");
			return;
		}
		
		else if(isEmpty() == true) // empty tree
		{
			root = newLeaf;
		}
		
		else
		{
			root.insert(root, newLeaf); // insert node
		}
	}
	
	// delete node from binary search tree
	public void delete(T data)
	{
		if(isEmpty() == true) // empty tree
		{
			System.out.println("cannot delete item in empty tree");
		}
		
		else
		{
			root.delete(root, data); // delete node
		}
	}
	
	// search node in binary search tree
	public void searchItem(T data)
	{
		if(isEmpty() == true) // empty tree
		{
			System.out.println("cannot find item in empty tree");
		}
		
		else
		{
			root.searchItem(root, data);
		}
	}
	
	// find number of nodes in binary tree
	public int size() 
	{ 
		if(isEmpty() == true) // empty tree
		{
			return 0;
		}
		
		else
		{
			return root.size();
		}
	}
	
	// find height of binary tree
	public int height() 
	{  
		if(isEmpty() == true) // empty tree
		{
			return -1;
		}
		
		else
		{
			return root.height(root) - 1;
		}
	}
	
	// list nodes in preOrder fashion
	public void preOrder() 
	{
		if(isEmpty() == true) // empty tree
		{
			return;
		}
		
		else
		{
			root.preOrder(elements);
		}
	}
	
	// list nodes in inOrder fashion
	public void inOrder() 
	{
		if(isEmpty() == true) // empty tree
		{
			return;
		}
		
		else
		{
			root.inOrder(elements);
		}
	}
	
	// list nodes in postOrder fashion
	public void postOrder() 
	{
		if(isEmpty() == true) // empty tree
		{
			return;
		}
		
		else
		{
			root.postOrder(elements);
		}
	}
	
	//////////////////////////////////// Accessors /////////////////////////////////////////////
	
	// find node with the largest data
	public T largest() 
	{ 
		if(isEmpty() == true) // empty tree
		{
			return null;
		}
		
		else
		{
			return root.largest();
		}
	}
	
	// find node with the smallest data
	public T smallest() 
	{ 
		if(isEmpty() == true) // empty tree
		{
			return null;
		}
		
		else
		{
			return root.smallest();
		}
	}
	
	// find middle node; [4]
	public T median() 
	{ 
		if(isEmpty() == true) // empty tree
		{
			return null;
		}
		
		else
		{
			List<T> temp = getElements();
			
			if((temp.size() % 2) == 0) // even number of nodes
			{
				int x = temp.size() - (temp.size() / 2) - 1;
				T u = temp.get(x);
				return u;
			}
			
			else // odd number of nodes
			{
				int y = ((temp.size() + 1) / 2) - 1;
				T v = temp.get(y);
				return v;
			}
		}
	}
}
