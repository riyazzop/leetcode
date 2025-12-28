# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:return []
        res=[]
        q=collections.deque([root])
        while q:
            qLen=len(q)
            rightNode=None
            for _ in range(qLen):
                node =q.popleft()
                if node:
                    rightNode=node
                    q.append(node.left)
                    q.append(node.right)
            if rightNode:
                res.append(rightNode.val)
        return res
        