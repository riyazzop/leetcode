class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        heapq.heapify(intervals)
        res=[]
        while intervals:
            start,end=heapq.heappop(intervals)
            if res and res[-1][1]>=start:
                start2,end2=res.pop()
                res.append([start2,max(end,end2)])
                continue
            res.append([start,end])
        return res