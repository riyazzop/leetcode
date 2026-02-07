class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[]
        for c in s:
            if not res or res[-1]!=c:
                res.append(c)
            else:
                res.pop()
        return ''.join(res)