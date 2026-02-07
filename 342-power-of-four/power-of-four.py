class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n-1)&n==0:
            if (n-1)%3==0:
                return True
        return False