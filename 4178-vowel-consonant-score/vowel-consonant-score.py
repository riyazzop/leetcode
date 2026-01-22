class Solution(object):
    def vowelConsonantScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels={'a','e','i','o','u'}
        vcnt=ccnt=0
        for c in s:
            if c in vowels:
                vcnt+=1
            else:
                if c.isalpha():
                    ccnt+=1
        if ccnt:
            return vcnt//ccnt
        return 0
        