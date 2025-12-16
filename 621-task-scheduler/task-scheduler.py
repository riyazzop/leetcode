class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count=Counter(tasks)
        maxHeap=[-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q=deque()#[cnt,idleTime]
        time=0
        while maxHeap or q:
            time+=1
            if maxHeap:
                cnt=1+heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                cnt=q.popleft()[0]
                heapq.heappush(maxHeap,cnt)
        return time
            
        