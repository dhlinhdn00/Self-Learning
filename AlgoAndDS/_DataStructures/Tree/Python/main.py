from Tree import Node, Tree

def main():
    # 1) Create a tree with root node 'A'
    tree = Tree("A")
    A = tree.root

    # 2) Add children 'B' and 'C' to 'A'
    B = Node("B")
    C = Node("C")
    A.addChild(B)
    A.addChild(C)

    # 3) Add children 'D', 'E', and 'F' to 'B'
    D = Node("D")
    E = Node("E")
    F = Node("F")
    B.addChild(D)
    B.addChild(E)
    B.addChild(F)

    # 4) Add children 'G' and 'H' to 'C'
    G = Node("G")
    H = Node("H")
    C.addChild(G)
    C.addChild(H)

    # 5) Add children 'I' and 'J' to 'D'
    I = Node("I")
    J = Node("J")
    D.addChild(I)
    D.addChild(J)

    # 6) Add child 'K' to 'I'
    K = Node("K")
    I.addChild(K)

    # === Demonstrate the methods ===
    
    # 1) Show parent of B
    parent_B = tree.getParent(B)
    print("Parent of B:", parent_B.data if parent_B else "None")
    
    # 2) Show children of A
    children_A = tree.getChildren(A)
    print("Children of A:", [child.data for child in children_A])
    
    # 3) Show root node
    print("Root node:", tree.root.data if tree.root else "None")
    
    # 4) Check if E is a leaf node
    print("Is E a leaf node?", "true" if tree.isLeaf(E) else "false")
    
    # Check if B is a leaf node
    print("Is B a leaf node?", "true" if tree.isLeaf(B) else "false")
    
    # 5) Show ancestors of K
    ancestors_K = tree.getAncestors(K)
    print("Ancestors of K:", [anc.data for anc in ancestors_K])
    
    # 6) Show descendants of D
    descendants_D = tree.getDescendants(D)
    print("Descendants of D:", [desc.data for desc in descendants_D])
    
    # 7) Show siblings of D
    siblings_D = tree.getSiblings(D)
    print("Siblings of D:", [sib.data for sib in siblings_D])
    
    # 8) Show levels of A, B, and D
    print("Level of A (root):", tree.getLevel(A))
    print("Level of B:", tree.getLevel(B))
    print("Level of D:", tree.getLevel(D))
    
    # 9) Check if A is an internal node
    print("Is A an internal node?", "true" if tree.isInternal(A) else "false")
    
    # Check if E is an internal node
    print("Is E an internal node?", "true" if tree.isInternal(E) else "false")
    
    # 10) Show neighbors of B
    neighbors_B = tree.getNeighbors(B)
    print("Neighbors of B:", [nbr.data for nbr in neighbors_B])
    
    # 11) Show the subtree rooted at D
    subtree_D = tree.getSubtree(D)
    print("Subtree rooted at D:", [sub.data for sub in subtree_D])
    
    # 12) Show all edges in the tree
    edges = tree.getEdges()
    print("All edges in the tree:", edges)


if __name__ == "__main__":
    main()