class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        i=0
        for char in s:
            if i<len(t) and char ==t[i]:
                i+=1
        return len(t)-i