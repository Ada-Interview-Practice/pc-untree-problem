# Consonants Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

We are interested in converting a binary tree into a dictionary.

For example:

```
           a
         /   \
        /     \
       x       y
      / \       \
     e   m       p
```

Would be converted to:

```py
{
    "a": ("x", "y"),
    "x": ("e", "m"),
    "y": (None, "p"),
    "e": (None, None),
    "m": (None, None),
    "p": (None, None),
}
```

Each key of the dictionary will be the data held by a parent node. Each value will be a tuple. The first element of the tuple will hold the data from the left child. The second element of the tuple will hold the data from the right child. If a node does not have a left and/or right child, the value in the corresponding spots in tuple will be None.

Write a function that takes in the root of a tree and returns a dictionary representation of the tree.

## Examples

### Example 1

The tree

```
       d
      / \
     e   v
```

produces the following dictionary

```py
{
    "d": ("e", "v"),
    "e": (None, None),
    "v": (None, None),
}
```

### Example 2

The tree

```
           a
         /   \
        /     \
       x       y
      / \       \
     e   m       p
```

produces the following dictionary

```py
{
    "a": ("x", "y"),
    "x": ("e", "m"),
    "y": (None, "p"),
    "e": (None, None),
    "m": (None, None),
    "p": (None, None),
}
```

### Example 3

The tree

```
           g
         /   \
        /     \
       e       f
      /         \
     k           d
    /             \
   w               z
```

produces the following dictionary

```py
{
    "g": ("e", "f"),
    "e": ("k", None),
    "k": ("w", None),
    "w": (None, None),
    "f": (None, "d"),
    "d": (None, "z"),
    "z": (None, None),
}
```

## Notes for the Interviewer

### Clarifying Questions

#### Q: What should I do if the input is None or has fewer than three nodes?

A: You can assume the tree will include at least three Nodes.

#### Q: Will the input contain any cycles?

A: No.

#### Q: What should I do if invalid input is passed in?

A: You can assume that the input will be valid.

#### Q: What data types will be stored in the values?

A: Strings.

#### Q: What should I do if there are duplicate values in the tree?

A: You can assume every value in the tree will be unique.

### Hints

- If your candidate struggles with an initial algorithm, encourage them to walk through an example and describe how they would do it using only pen and paper.

- If your candidate struggles to determine how to do the iteration / recursion, encourage them to first do the simpler case where there is only one parent with two children (the first test case). If they complete that case, they can revisit the logic to traverse the tree.

- Encourage your candidate to print the result if they are not passing the test cases and are unsure why. If their dictionary contains the actual node objects, remind them that we want the dictionary to hold the data stored in the nodes, not the nodes themselves.

## Optional Bonus At-Home Challenges

To be attempted after completing the interview.

- What are the time/space complexities of the sample solution? Does it make a difference whether the tree is balanced or not?

- What are the tradeoffs between storing this data using nodes vs using a dictionary? Which do you prefer in what cases?

- If you wrote a recursive solution, try writing an iterative one. If you wrote an iterative solution, try writing a recursive one. Which do you prefer? What are the tradeoffs?

- Modify the Node class so that each node can have any number of children. Modify your solution to handle representing these new trees.

### Extra Hard Challenge

- Can you think of how to represent a binary tree using only a single dimensional list? Make it so finding the root is O(1) and finding the children of a given node is also O(1). What are the tradeoffs of storing a binary tree in this format?
