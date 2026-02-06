class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        length=sum(matchsticks)//4
        matchsticks.sort(reverse=True)
        if sum(matchsticks)/4!=length:
            return False
        sides=[0]*4
        def backtrack(i):
            if i==len(matchsticks):
                return True
            for j in range(4):
                if j>0 and sides[j]==sides[j-1]:
                    continue
                if sides[j]+matchsticks[i]<=length:
                    sides[j]+=matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[j]-=matchsticks[i]
            return False
        return backtrack(0)
                    
        