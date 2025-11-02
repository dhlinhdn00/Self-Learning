from BFS import bfs
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from DataStructures.Tree.Python.Tree import Tree, Node

def main():
    tree = Tree('A')
    
    # Create other nodes
    nodeB = Node('B')
    nodeC = Node('C')
    nodeD = Node('D')
    nodeE = Node('E')
    nodeF = Node('F')
    nodeG = Node('G')
    
    # Build the tree:
    #          A
    #         / \
    #        B   C
    #       / \   \
    #      D   E   F
    #             /
    #            G
    tree.root.addChild(nodeB)
    tree.root.addChild(nodeC)
    nodeB.addChild(nodeD)
    nodeB.addChild(nodeE)
    nodeC.addChild(nodeF)
    nodeF.addChild(nodeG)
    
    # Execute BFS traversal
    bfs_result = bfs(tree)
    
    # Print the order of nodes visited in BFS
    print("BFS traversal order:", [node.data for node in bfs_result])
    
    # If you want to search for a specific target, e.g., node with data 'F':
    bfs_until_F = bfs(tree, target_data='F')
    print("BFS traversal until 'F':", [node.data for node in bfs_until_F])

if __name__ == '__main__':
    main()