"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q=collections.deque([root])
        res=[]
        while q:
            qLen=len(q)
            level=[]
            for i in range(qLen):
                node=q.popleft()
                level.append(node.val)
                if root.children:
                    for child in node.children:
                        q.append(child)
            res.append(level)
        return res 

        