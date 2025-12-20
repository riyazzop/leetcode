class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones=[-stn for stn in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            stn1=abs(heapq.heappop(stones))
            stn2=abs(heapq.heappop(stones))
            if stn1>stn2:
                heapq.heappush(stones,-(stn1-stn2))
        return -stones[0] if stones else 0
            


