
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        notebook = []
        self.visit(root, notebook)
        return notebook

    def visit(self, node, notebook):
        if node is None:
            return
        self.visit(node.left, notebook)
        notebook.append(node.val)
        self.visit(node.right, notebook)

                
        


# if an item has no left or right, it's a leaf, and you can go back one
# if a value has a left but no right, go left
# if a value has a right but no left, check the number after that

"""
left? => yes => previous is root(1), root is left(7)
left? => yes => previous is root(7), root is left(2)
left? => no => right? => no => push root(2), root is previous
left? => no => right? => yes => previous is root(7), root is right(6)
left? => yes => previous is root(6), root is left (5)
"""
# ex. push 1, go