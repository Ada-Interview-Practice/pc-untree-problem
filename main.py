# DO NOT MODIFY THE NODE CLASS!
class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def traverse_and_fill(node, to_fill):
    ''' 
    Helper function to recursively traverses the tree, adding keys/values
    to to_fill dictionary. Keys are the data the parent nodes hold,
    values are a tuple with the data the left and right children hold.
    '''
    
    # No need to alter the dictionary if the tree is empty
    if node is None:
        return

    # Default the data from the left and right nodes to None
    left_val, right_val = None, None

    # Only replace the data for each if each child is not None
    if node.left:
        left_val = node.left.value
    if node.right:
        right_val = node.right.value

    # Mutate the dictionary
    # Parent data is key
    # Child data is put into tuples
    to_fill[node.value] = (left_val, right_val)

    # Recurse down each subtree
    traverse_and_fill(node.left, to_fill)
    traverse_and_fill(node.right, to_fill)

def convert(tree):
    # Initialize empty dictionary that will be mutated to hold
    # the results
    result = {}
    # Traverse tree, mutating the result dictionary
    traverse_and_fill(tree, result)
    return result



r"""
       d
      / \
     e   v
"""
tree = Node("d", Node("e"), Node("v"))
assert convert(tree) == {
    "d": ("e", "v"),
    "e": (None, None),
    "v": (None, None),
}

r"""
           a
         /   \
        /     \
       x       y
      / \       \
     e   m       p
"""
tree = Node("a", Node("x", Node("e"), Node("m")), Node("y", None, Node("p")))
assert convert(tree) == {
    "a": ("x", "y"),
    "x": ("e", "m"),
    "y": (None, "p"),
    "e": (None, None),
    "m": (None, None),
    "p": (None, None),
}

r"""
           g
         /   \
        /     \
       e       f
      /         \
     k           d
    /             \
   w               z
"""
tree = Node("g", Node("e", Node("k", Node("w"))), Node("f", None, Node("d", None, Node("z"))))
assert convert(tree) == {
    "g": ("e", "f"),
    "e": ("k", None),
    "k": ("w", None),
    "w": (None, None),
    "f": (None, "d"),
    "d": (None, "z"),
    "z": (None, None),
}

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
