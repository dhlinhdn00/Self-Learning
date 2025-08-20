#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// ========================
// 1) Define the Node class
// ========================
class Node {
public:
    string data;              // Data stored in the node
    Node* parent;             // Pointer to the parent node
    vector<Node*> children;   // List of child nodes
    
    // Constructor
    Node(const string& value) : data(value), parent(nullptr) {}
    
    // Method to add a child to this node
    void addChild(Node* child) {
        children.push_back(child);
        child->parent = this;
    }
};

// ========================
// 2) Define the Tree class
// ========================
class Tree {
public:
    Node* root;  // The root of the tree
    
    // Constructor: create a Tree with a given root value
    Tree(const string& rootData) {
        root = new Node(rootData);
    }
    
    // 2.1. Get the parent of a node
    Node* getParent(Node* node) {
        return node ? node->parent : nullptr;
    }
    
    // 2.2. Get the children of a node
    vector<Node*> getChildren(Node* node) {
        if (node) {
            return node->children;
        }
        return {};
    }
    
    // 2.3. Check if a node is a leaf (no children)
    bool isLeaf(Node* node) {
        return node && node->children.empty();
    }
    
    // 2.4. Get all ancestors of a node
    vector<Node*> getAncestors(Node* node) {
        vector<Node*> ancestors;
        Node* current = node->parent;
        while (current != nullptr) {
            ancestors.push_back(current);
            current = current->parent;
        }
        return ancestors;
    }
    
    // 2.5. Get all descendants of a node
    vector<Node*> getDescendants(Node* node) {
        vector<Node*> descendants;
        getDescendantsHelper(node, descendants);
        return descendants;
    }
    
    // Helper function for getDescendants
    void getDescendantsHelper(Node* node, vector<Node*>& result) {
        if (!node) return;
        for (auto* child : node->children) {
            result.push_back(child);
            getDescendantsHelper(child, result);
        }
    }
    
    // 2.6. Get all siblings of a node
    vector<Node*> getSiblings(Node* node) {
        vector<Node*> siblings;
        if (!node || !node->parent) return siblings;
        
        for (auto* child : node->parent->children) {
            if (child != node) {
                siblings.push_back(child);
            }
        }
        return siblings;
    }
    
    // 2.7. Get the level (depth) of a node
    //      (the number of edges on the path from the root to this node)
    int getLevel(Node* node) {
        int level = 0;
        Node* current = node;
        while (current && current->parent != nullptr) {
            level++;
            current = current->parent;
        }
        return level;
    }
    
    // 2.8. Check if a node is internal (has at least one child)
    bool isInternal(Node* node) {
        return node && !node->children.empty();
    }
    
    // 2.9. Get all neighbors (parent + children) of a node
    vector<Node*> getNeighbors(Node* node) {
        vector<Node*> neighbors;
        if (!node) return neighbors;
        
        if (node->parent != nullptr) {
            neighbors.push_back(node->parent);
        }
        for (auto* child : node->children) {
            neighbors.push_back(child);
        }
        return neighbors;
    }
    
    // 2.10. Get the subtree rooted at a particular node (node + all its descendants)
    vector<Node*> getSubtree(Node* node) {
        vector<Node*> subtree;
        if (!node) return subtree;
        
        subtree.push_back(node);
        // Add all descendants
        getDescendantsHelper(node, subtree);
        return subtree;
    }
    
    // 2.11. Get all edges in the tree as a list of (Parent - Child)
    vector<string> getEdges() {
        vector<string> edges;
        getEdgesHelper(root, edges);
        return edges;
    }
    
    // Helper for getEdges
    void getEdgesHelper(Node* node, vector<string>& edges) {
        if (!node) return;
        for (auto* child : node->children) {
            edges.push_back("(" + node->data + " - " + child->data + ")");
            getEdgesHelper(child, edges);
        }
    }
};

// ========================
// 3) Test in the main()
// ========================
int main() {
    // 1) Create the tree with root "A"
    Tree tree("A");
    Node* A = tree.root;
    
    // 2) Add children B, C to A
    Node* B = new Node("B");
    Node* C = new Node("C");
    A->addChild(B);
    A->addChild(C);
    
    // 3) Add children D, E, F to B
    Node* D = new Node("D");
    Node* E = new Node("E");
    Node* F = new Node("F");
    B->addChild(D);
    B->addChild(E);
    B->addChild(F);
    
    // 4) Add children G, H to C
    Node* G = new Node("G");
    Node* H = new Node("H");
    C->addChild(G);
    C->addChild(H);
    
    // 5) Add children I, J to D
    Node* I = new Node("I");
    Node* J = new Node("J");
    D->addChild(I);
    D->addChild(J);
    
    // 6) Add child K to I
    Node* K = new Node("K");
    I->addChild(K);
    
    // === Demonstrate the methods ===
    
    // 1) Parent Node
    cout << "Parent of B: " << (tree.getParent(B) ? tree.getParent(B)->data : "None") << endl;
    
    // 2) Child Nodes of A
    cout << "Children of A: ";
    for (auto* child : tree.getChildren(A)) {
        cout << child->data << " ";
    }
    cout << endl;
    
    // 3) Root Node
    cout << "Root node: " << (tree.root ? tree.root->data : "None") << endl;
    
    // 4) Leaf Node
    cout << "Is E a leaf node? " << (tree.isLeaf(E) ? "true" : "false") << endl;
    cout << "Is B a leaf node? " << (tree.isLeaf(B) ? "true" : "false") << endl;
    
    // 5) Ancestors of K
    cout << "Ancestors of K: ";
    for (auto* ancestor : tree.getAncestors(K)) {
        cout << ancestor->data << " ";
    }
    cout << endl;
    
    // 6) Descendants of D
    cout << "Descendants of D: ";
    for (auto* desc : tree.getDescendants(D)) {
        cout << desc->data << " ";
    }
    cout << endl;
    
    // 7) Siblings of D
    cout << "Siblings of D: ";
    for (auto* sib : tree.getSiblings(D)) {
        cout << sib->data << " ";
    }
    cout << endl;
    
    // 8) Level
    cout << "Level of A (root): " << tree.getLevel(A) << endl;
    cout << "Level of B: " << tree.getLevel(B) << endl;
    cout << "Level of D: " << tree.getLevel(D) << endl;
    
    // 9) Internal Node
    cout << "Is A an internal node? " << (tree.isInternal(A) ? "true" : "false") << endl;
    cout << "Is E an internal node? " << (tree.isInternal(E) ? "true" : "false") << endl;
    
    // 10) Neighbors of B
    cout << "Neighbors of B: ";
    for (auto* neighbor : tree.getNeighbors(B)) {
        cout << neighbor->data << " ";
    }
    cout << endl;
    
    // 11) Subtree at D
    cout << "Subtree rooted at D: ";
    for (auto* sub : tree.getSubtree(D)) {
        cout << sub->data << " ";
    }
    cout << endl;
    
    // 12) Edges in the tree
    vector<string> edges = tree.getEdges();
    cout << "All edges in the tree: ";
    for (auto& edge : edges) {
        cout << edge << " ";
    }
    cout << endl;

    return 0;
}
