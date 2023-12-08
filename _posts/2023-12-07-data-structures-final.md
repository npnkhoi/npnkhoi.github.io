---
layout: post
title: Data Structures and Algorithms - Final Exam Review
tags: cs
---

Previously: [Midterm Review]({%post_url 2023-10-10-data-structures-midterm%})

## [[Red-Black Tree]]

Properties:
1. Every node is either red or black. 
2. The root is black
3. Leaf nodes are NIL and black
4. No to adjacent red nodes
5. For each node, all paths from it to leaves contain the same number of black nodes.

=> So, Black nodes carries a fixed weight, while red node is hot. The goal is to (1) balance the weight and (2) not creating fire by putting hot things together.

Insertion:
- Insert the new node just like a binary search tree, in Red
- (Recursive) If the parent of the new node is red, there are 2 consecutive reds. We look at the **uncle** (sibling of parent).
	- **If the uncle is black**, "rotate" the triplet at the grandparent towards that uncle
		- (if zigzag), rotate like AVL to make straight line.
		- (now having straight line) Purpose is to put the red node to the other side. Therefore, beside rotating the values, "throw" the red to the other side
	- **If the uncle is red**
		- change the parent and uncle to black
		- if the grand parent is not the root, change it to Red (to protect the relationship with the rest of the tree)
		- if it creates double red, continue recursively for the nodes above

Deletion:
- Similar to AVL: Find the node. Bring its predecessor/successor to replace it
- If there is a shortage of black at the newly vacant space (because the deleted node), which is now a NIL leaf, we start by putting a square at that node. This square represent **extra blackness**. 
- Do the following recursively:
	1. If the node itself is red: Change to black and done.
	2. Otherwise, if the sibling is red:
		- rotate to bring the red to the shortage area.
		- Keep the square where it is. Now re-evaluate the problem. There is now a non-NIL black sibling (case 4). Go there.
	3. Otherwise, if the nephew is red:
		- rotate to bring the red to the shortage area. Then change it to black. **No problem anymore, break the loop.**
	4. Otherwise, there must be a black sibling. Change that sibling to red and move the square up. (it's now the problem of the parent). Recurse.
## [[Hashing]]

Basics:
- Hash functions (for either numbers or string) -- usually provided.
- Basic insertion: Use the hash value for the key, modulo them by the table size to get a bucket number, then insert the value to the "bucket".

Collision handling:
- **Separate Chaining**: keep a linked list of the items at the same index
	- new item: add to one end of the list
	- search: traverse the list
- **Open Addressing**: finding another cell in the table
	- **Linear Probing**:
		- should only be used when load factor < 0.5 (to avoid too much collision)
		- problem: primary clustering
	- **Quadratic Probing**: when colliding, `new key = original key + i^2` (for i from 1)
		- helps avoid *primary clustering* (things are too close to each other?)
		- if cannot find a place for an item, or just when the table is half full -- load factor >= 0.5:
			- double the table, then increase to the next prime number
			- "rehashing": traverse the table from left to right, relocate (in a new array)
	- Double hashing: second hash function?
		- base = hash(key) % size
		- offset = (collision number) x (hash2(key))
		- new key = base + offer
## [[B-Tree]]
B-Tree is a self-balanced Multi-way Search Tree, with height different is 0 everywhere. To maintain that, we need:
- Internal nodes
	- Max: m children, m-1 keys
	- Min: ceil(m/2) children, ceil(m/2)-1 keys
	- (Non-leaf) root node
		- Min 2 children
	- If k children, then k-1 keys
- Leaves: all on the same level

Operations
- INSERT
	- add the new value to the appropriate LEAF node
		- If not leaf, there will be an imbalance (e.g., k keys, k children)
	- if a node is overflow (more than n-1 keys)
		- move the middle key up
			- may create new node
			- or join with the existing parent
		- break the two parts down to be two children OF THE NEW PARENT KEY.
- DELETE
	- Loss of keys is always in the leaf node. Move the predecessor or successor up to the deleted position
	- If "underflow" happens at a node. (1)
		- If can borrow from a sibling, borrow by *rotation*. During rotation, also bring the child of the "escalated" key to the other branch.
		- If cannot, bring the parent *key* of itself down with one sibling; merging into 3 into one node
		- then the parent *node* may be underflow (even having 0 keys), just fix recursively from (1)
## [[AVL Tree]]

Is a type of self-balancing [[Binary Search Tree]] where:
- the height difference of the two children must not exceed 1.
- the Node struct now maintains the `height`

- insert
	- insert normally first
	- traverse upwards from the new node until there is height violation
	- if there is a violation, mark the nodes 1 2 3 downwards (along the up-path)
		- there is always at least 2 nodes below 1 along that path
	- check the shape of 1-2-3 (4 possible shapes)
		- straight lines are easy
		- zigzag is harder
- delete
	- first, delete the node using the pre/suc algorithm
	- start checking imbalance from the parent of the delete node (which is either the node we actually want to delete, the pred, or the succ -- they are always a leaf)
	- "fix" any imbalance and NOT STOP THERE, continue up until reach the root

## [[Radix Sort]]

This is a generalization of counting sort. "Radix" is the alphabet size. It's 10 for decimal.

**Most significant digit first**
Think of the numbering system as a tree with branching factor R. The elements are leaf nodes of that with branching factor R. Radix sort here is just an in-order traversal, which shows the sorted list.

Time complexity: O(NM), where M is log_R(max value)

**Least significant digit first**

Idea: At time t, make sure all the numbers are sorted by t least significant digits. Put them into buckets according to the (t-1)-th digit. Now all elements are sorted by (t+1) least significant digits. And it goes on.
## Misc
- [[Union-Find]]
- MST: [[Prim algorithm]] returns a different tree from [[Dijsktra algorithm]]
- Strong connectedness
- Transitive closure