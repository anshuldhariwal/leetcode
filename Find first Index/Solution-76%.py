class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """        
        # try:
        #     value = haystack.index(needle)
        # except:
        #     return -1
        # return  value

        p1 = 0
        p2 = 0
        while p1 <= len(haystack):
            if p2 == len(needle):
                return p1-len(needle)
            elif p1 == len(haystack):
                return -1
            if haystack[p1] == needle[p2]:
                p2 += 1
            else:
                p1 = p1 - p2
                p2 = 0
            
            p1 += 1       
