class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        trips.sort(key=lambda t:t[1])
        minHeap=[]
        curPass=0
        for trip in trips:
            numPass,start,end=trip
            while minHeap and minHeap[0][0]<=start:
                curPass-=minHeap[0][1]
                heapq.heappop(minHeap)
            curPass+=numPass
            if curPass>capacity:
                return False
            heapq.heappush(minHeap,[end,numPass])
        return True
        