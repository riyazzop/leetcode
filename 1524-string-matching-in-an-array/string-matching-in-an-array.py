class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res=[]
        for i,word in enumerate(words):
            for j,word2 in enumerate(words):
                if len(word2)>len(word):
                    if i!=j:
                        if word in word2:
                            res.append(word)
                            break
        return res
        