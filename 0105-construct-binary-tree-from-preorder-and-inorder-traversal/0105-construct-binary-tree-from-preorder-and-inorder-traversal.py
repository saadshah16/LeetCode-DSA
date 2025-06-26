# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Building a hashmap for quick index lookup
        inorder_hm = {val:idx for idx,val in enumerate(inorder)}

        # Preorder index
        preorder_idx = 0

        def helper(left:int , right: int) -> Optional[TreeNode]:
            nonlocal preorder_idx
            if left > right:
                return None
            
            # Build current root
            root_val = preorder[preorder_idx]
            preorder_idx += 1
            root = TreeNode(root_val)

            # Get the index of the root in inroder
            index = inorder_hm[root_val]

            # Recursively build left and right subtrees
            root.left = helper(left,index-1)
            root.right = helper(index + 1, right)

            return root
        
        return helper(0,len(inorder)-1)
        # TC: O(n) - Each node is processed once
        # SC: O(n) - For hashmap + call stack
        
        
        
        
        # The below solution is not optimal as slicing and .index takes O(n) lookup
        # if not preorder or not inorder:
        #     return None
        
        # root = TreeNode(preorder[0]) # First element is always the root
        # mid = inorder.index(preorder[0]) # Get index of the root in inorder to split left/right

        # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # return root

        # TC: O(n^2)
        # SC: O(n^2)