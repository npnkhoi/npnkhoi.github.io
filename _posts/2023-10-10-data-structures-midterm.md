---
layout: post
title: Data Sructures Review
---

*A review for the midterm of CS5343*

- Analysis
    - Running time: Trick is to count how many times a line is considered
    - Big O rules
    - Recursion
- List
    - Array
        -  In Java, Array resizing is copying the whole array to a newly sized array.
    - Linked list: singly and doubly linked
    - Stack
    - Queue
- Tree
    - Generic binary tree
        - Properties: depth of a node, height of a tree
        - Components: root, internal nodes, leaf nodes
        - Types: 
            - Full binary tree: each node has 0 or 2 children.
            - Complete binary tree: all nodes except the last level have 2 children, and all last-level nodes are on the left.
        - Problems: mirroring (inplace), 
    - Binary search tree
        - Insert in O(logN): trivial
        - Delete in O(logN):
            - find the node (called $u$), return if not found
            - bring the predecessor or successor (called $v$) to 'replace' the found node. Replace is best done by value assignment?
                - $v$ has at most 1 child on a known side. Attach that child to the former parent of $v$ on the other side.
                    - Tricky case: u is the parent of v.
    - AVL tree
        - Balancing:
            - Condition: Height difference between two branches of the same parent is at most 1.
            - Fixing algorithm: straight or zigzag
        - Insert: Insert, go up and fix
        - Delete: Delete like normal, go up and fix
    - Heap:
        - Properties: structure, value
        - Representation: 1-based array, 0-th element stores the size
        - Insert: insert at the end of the array, then keep swapping if up if needed.
        - Pop: bring last child to the root, and "percolate" it down
    - B-Trees
        - Properties: 0 height difference. That means:
            - internal nodes has at least ceil(m/2) children
            - leaf nodes has at least 2 children
            - leafs all on the same level
        - Insert: First, insert into an existing node. If overflow (m keys), bring the middle key up and split to two children.
        - Delete: (need revision)
            - First, bring the predecessor or successor up to the found node.  
            - If underflow happens:
                - First, try borrowing from a sibling without making them underflow.
                - If not, both children can be merge with the parent. Bring the parent key down.
                - If the parent node is underflow, fix recursively.
- Sorting algorithms
    - Bubble sort: keep going through the array from left to right and swap if violation.
    - Insertion sort: Keep getting the smallest element to the front of the unsorted part (by swapping).
    - Merge sort: trivial
    - Heap sort: heapify the array (Floyd's method, O(N) at worst!), then pop all

P/S: This is the class in which I sat and [daydreamt about AGI]({%post_url 2023-08-24-ai%}).