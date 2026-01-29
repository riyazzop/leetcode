class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        def dfs(i,cur):
            if i==len(nums):
                res.append(cur[:])
                return
            cur.append(nums[i])
            dfs(i+1,cur)
            cur.pop()
            while i<len(nums)-1 and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1,cur)
        dfs(0,[])
        return res