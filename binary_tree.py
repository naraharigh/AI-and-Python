# Define a Node class for the binary tree
'''

Let’s restate traversal definitions:
Traversal	Visit Order	Root Position	Visualization
Preorder	Root → Left → Right	Root is visited first	Think: "Top-down"
Inorder	Left → Root → Right	Root is visited in the middle	Think: "Left-to-right"
Postorder	Left → Right → Root	Root is visited last	Think: "Bottom-up"


My commnets:


Left -- Right same

Pre  order means before left right 
In  order menas between 
Post order t after left right

'''






class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# In-order traversal (Left, Root, Right)
def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.value, end=' ')
        in_order_traversal(root.right)

# Pre-order traversal (Root, Left, Right)
def pre_order_traversal(root):
    if root:
        print(root.value, end=' ')
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

# Post-order traversal (Left, Right, Root)
def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.value, end=' ')

# Level-order traversal using a queue
from collections import deque


def vertical_traversal(root):
    if not root:
        return []
    
    hd_map = defaultdict(list)
    queue = deque([(root, 0)])  # (node, horizontal distance)
    
    while queue:
        node, hd = queue.popleft()
        hd_map[hd].append(node.value)
        
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    
    # Sort by HD and return grouped values
    return [hd_map[hd] for hd in sorted(hd_map.keys())]

def level_order_traversal(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Example usage
if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    print("In-order traversal:")
    in_order_traversal(root)
    print("\nPre-order traversal:")
    pre_order_traversal(root)
    print("\nPost-order traversal:")
    post_order_traversal(root)
    print("\nLevel-order traversal:")
    level_order_traversal(root)
