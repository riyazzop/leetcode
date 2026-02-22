class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        for i,interval in enumerate(intervals):
            if newInterval[1]<interval[0]:
                res.append(newInterval)
                return res+intervals[i:]
            elif newInterval[0]>interval[1]:
                res.append(interval)
            else:
                newInterval=[min(interval[0],newInterval[0]),max(interval[1],newInterval[1])]
        res.append(newInterval)
        return res

        