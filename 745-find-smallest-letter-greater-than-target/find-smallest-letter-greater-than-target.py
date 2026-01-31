class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for c in letters:
            # print(ord(target)-ord(c))
            if ord(c)-ord(target)>0:
                return c
        return letters[0]