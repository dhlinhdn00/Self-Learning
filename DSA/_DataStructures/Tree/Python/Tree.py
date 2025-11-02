class Node:
    def __init__(self, data: str):
        """
        Represents a single node in a tree. Each node has:
            :type data: str - The value stroed in the node
            :type parent: Node - A reference to its parent node (None if it is the root)
            :type children: List[Node] - A list of its child nodes
        """
        self.data = data
        self.parent = None
        self.children =  []

    
    def addChild(self, child: 'Node'): 
        # Using 'Node' instead of Node here is "Forward reference".
        # This means that type checking will recognize that the data type of child is Node.
        # But it will only be accurately mapped after the Node class is fully defined.
        """
        Add a child node and set the child's parent to this node.
        Also set the child's parent to be current node.
        """
        self.children.append(child)
        child.parent = self 

class Tree:
    """
    Represent a tree structure that holds a reference to its rood node.
    Contains various methods to traverse and query the tree.
    """
    def __init__(self, root_data: str):
        """
        Initialize the tree with a single root node having the given root_data
        """
        self.root = Node(root_data)

# ___________________________________________________________
# More Methods to get info of basic terminologies

    def getParent(self, node: Node):
        """
        Return a list of the parent of the given node.
        """
        return node.parent if node else []
    
    def getChildren(self, node: Node):
        """
        Return a list of the children of the given node.
        """
        return node.children if node else []

    def isLeaf(self, node: Node):
        """
        Return True if the node is a leaf, otherwise False.
        """
        return bool(node) and len(node.children) == 0

    def getAncestors(self, node: Node):
        """
        Return a list of all ancestor nodes (from the parent up to root, not including the node itself).
        """
        ancestors = []
        current = node.parent
        while current is not None:
            ancestors.append(current)
            current = current.parent
        return ancestors

    def getDescendants(self, node: Node):
        """
        Return a list of all descendants of the given node.
        """
        descendants = []
        self.getDescendantsHelper(node, descendants)
        return descendants

    def getDescendantsHelper(self, node: Node, result: list):
        """
        Helper method (recursive) to gather all descendants of a node.
        """
        if not node:
            return
        for child in node.children:
            result.append(child)
            self.getDescendantsHelper(child, result)
    
    def getSiblings(self, node: Node):
        """
        Return a list of sibling nodes of the given node.
        """
        siblings = []
        if node and node.parent:
            for child in node.parent.children:
                if child != node:
                    siblings.append(child)
        return siblings
    
    def getLevel(self, node: Node):
        """
        Return the level (depth) of the node, which is the number of edges from the root to the node.
        """
        level = 0
        current = node
        while current and current.parent is not None:
            level += 1
            current = current.parent
        return level
    
    def isInternal(self, node: Node):
        """
        Return True if it is internal, otherwise False.
        """
        return node is not None and len(node.children) > 0
    
    def getNeighbors(self, node: Node):
        """
        Return a list of neighbors of the given node. Neighbors include the parent and all direct children.
        """
        neighbors = []
        if node is None:
            return neighbors
        
        if node.parent is not None:
            neighbors.append(node.parent)

        for child in node.children:
            neighbors.append(child)
        
        return neighbors

    def getSubtree(self, node: Node):
        """
        Return a list containing the subtree of the given node. The subtree includes the node itself and all of its descendants.
        """
        subtree = []

        if node is None:
            return subtree
        
        subtree.append(node)

        self.getDescendantsHelper(node, subtree)

        return subtree

    def getEdges(self):
        """
        Return a list of all edges in the tree, formatted as string "(ParentData - ChildData)".
        """
        edges = []
        self.getEdgesHelper(self.root, edges)
        return edges

    def getEdgesHelper(self, node: Node, edges: list):
        """
        Helper method (recursive) to collect all parent-child edges from the node downwards.
        """
        if not node:
            return
        for child in node.children:
            edges.append(f"({node.data} - {child.data})")
            self.getEdgesHelper(child, edges)


    
