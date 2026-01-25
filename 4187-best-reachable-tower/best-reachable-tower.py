class Solution(object):
    def bestTower(self, towers, center, radius):
        """
        :type towers: List[List[int]]
        :type center: List[int]
        :type radius: int
        :rtype: List[int]
        """
        reachables=[tower for tower in towers if abs(tower[0]-center[0])+abs(tower[1]-center[1])<=radius]
        res=[-1,-1,-1]
        for tower in reachables:
            if tower[2]>res[2]:
                res=tower
            if tower[2]==res[2]:
                if tower[0]<res[0]:
                    res=tower
                if tower[0]==res[0] and tower[1]<res[1]:
                    res=tower
        return res[:2]





        