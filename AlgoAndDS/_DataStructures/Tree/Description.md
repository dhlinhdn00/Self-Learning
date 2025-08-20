# Tree

## Info

**Link**: https://www.geeksforgeeks.org/introduction-to-tree-data-structure/

---

## Summary:

Basic Terminologies in Tree:
- **Parent Node**: The node which is an immediate predecessor of a node is called the parent node of that node. 
- **Child Node**: The node which is the immediate successor of a node is called the child node of that node. 
- **Root Node**: The topmost node of a tree or the node which does not have any parent node is called the root node. A non-empty tree must contain exactly one root node and exactly one path from the root to all other nodes of the tree.
- **Leaf Node or External Node**: The nodes which do not have any child nodes are called leaf nodes. 
- **Ancestor of a Node**: Any predecessor nodes on the path of the root to that node are called Ancestors of that node. 
- **Descendant**: A node x is a descendant of another node y if and only if y is an ancestor of x.
- **Sibling**: Children of the same parent node are called siblings.
- **Level of a node**: The count of edges on the path from the root node to that node. The root node has level 0.
- **Internal node**: A node with at least one child is called Internal Node.
- **Neighbour of a Node**: Parent or child nodes of that node are called neighbors of that node.
- **Subtree**: Any node of the tree along with its descendant.
- **Edge**: The connection between two nodes in a tree is called an edge. It represents the relationship between a parent node and its child node.

### Example

                  A
                /   \
              B       C
           /  |  \   |  \
         D   E   F   G   H
       /  \
      I    J
      |
      K

1. Parent Node: Node A is the parent of B and C.
2. Child Node: Node G and F are children of A.
3. Root Node: A is the root node.
4. Leaf Node or External Node: E, F, G, H. J and K are leaf nodes.
5. Ancestor of a Node: Ancestors of K are I, D, B, and A.
6. Descendant: Descendants of D are I, J, and K.
7. Siblings: D, E and F are siblings.
8. Level of a Node:A is at level 0;  B and C are at level 1; D, E, F, G, and H are at level 2.
9. Internal Node: A, B and D are internal nodes.
10. Neighbor of a Node: Neighbors of B are A, D, E and F.
11. Subtree: The subtree rooted at D includes D, I, J, and K.
        D   
       /  \
      I    J
      |
      K
12. Edge: AB is an edge between A and B
