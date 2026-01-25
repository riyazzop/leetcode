class Solution(object):
    def rotateElements(self, nums, k):
        posarr = [n for n in nums if n >= 0]
        if not posarr:
            return nums
        k=k%len(posarr)
        posarr=posarr[k:]+posarr[:k]
        print(posarr)
        idx=0
        for i in range(len(nums)):
            if nums[i]>=0:
                nums[i]=posarr[idx]
                idx+=1
        return nums