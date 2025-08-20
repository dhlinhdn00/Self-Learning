from collections import deque
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from DataStructures.Tree.Python.Tree import Tree, Node

def bfs(tree: Tree, target_data: str = None):
    """
    Perform Breadth-First Search (BFS) on the tree and return a list of nodes 
    in the order they were visited. If target_data is provided, the function
    will stop and return the visited nodes as soon as it finds a node with matching data.

    :param tree: The tree to traverse (an instance of Tree)
    :param target_data: The data of the node to search for (optional)
    :return: A list of nodes visited in BFS order.
    """
    if tree.root is None:
        return []
    
    visited = []
    queue = deque()
    queue.append(tree.root)
    
    while queue:
        current = queue.popleft()
        visited.append(current)
        
        # If target_data is provided and the current node's data matches,
        # return the visited nodes immediately.
        if target_data is not None and current.data == target_data:
            return visited
        
        # Enqueue all the child nodes of the current node.
        for child in current.children:
            queue.append(child)
    
    return visited
