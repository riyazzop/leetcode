class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # k=k%len(s)
        return s[:k][::-1]+s[k:]
        