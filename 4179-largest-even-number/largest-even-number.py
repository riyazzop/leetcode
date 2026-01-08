class Solution(object):
    def largestEven(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=len(s)-1
        # print(s[i])
        while s and int(s[i])!=2:
            s=s[:i]
            i-=1
        return s