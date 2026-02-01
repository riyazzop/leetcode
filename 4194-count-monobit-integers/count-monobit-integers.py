class Solution(object):
    def countMonobit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        count=1
        val=1
        while val<=n:
            count+=1
            val=(val<<1)| 1
        
        return count
        