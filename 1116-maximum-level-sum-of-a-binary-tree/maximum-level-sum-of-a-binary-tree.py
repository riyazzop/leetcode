# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res=0
        q=deque([root])
        maxsum=float('-inf')
        level=0
        while q:
            level+=1
            levelsum=0
            for _ in range(len(q)):
                node=q.popleft()
                levelsum+=node.val
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)
            if levelsum>maxsum:
                maxsum=levelsum
                res=level
        return res