# Python code for Vertical Traversal of a Binary Tree 
# using HashMap and DFS (Depth First Search)

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# Helper function to perform DFS and 
# store nodes at different horizontal distances
def DFS(root, hd, mn, mp):
    if root is None:
        return
    print (hd)
    # Store the current node in the map at horizontal distance hd
    if hd not in mp:
        mp[hd] = []
    mp[hd].append(root.data)
    
    # Update the minimum horizontal distance
    mn[0] = min(mn[0], hd)
    
    # Recursively traverse the left and right subtrees
    DFS(root.left, hd - 1, mn, mp)
    DFS(root.right, hd + 1, mn, mp)

# Function to perform vertical order traversal of a binary tree
def verticalOrder(root):
    # Dictionary to store nodes at each horizontal distance
    mp = {}
    
    # List to track the minimum horizontal distance (mutable)
    mn = [0]

    # Perform DFS to fill the dictionary with vertical levels
    DFS(root, 0, mn, mp)
    
    res = []
    hd = mn[0]

    # Traverse the dictionary from minimum to maximum horizontal distance
    while hd in mp:
        res.append(mp[hd])
        hd += 1

    return res

if __name__ == "__main__":
    # Constructing the binary tree:
    #        1
    #       / \
    #      2   3
    #     / \ / \
    #    4  5 6  7
    #          \  \
    #           8  9
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(55)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)
    root.right.right.right.right = Node(99)

    res = verticalOrder(root)
    
    for temp in res:
        print("[", " ".join(map(str, temp)), "]", end=" ")
