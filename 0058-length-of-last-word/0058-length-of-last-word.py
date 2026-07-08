class Solution(object):
    def lengthOfLastWord(self, s):
        count=0
        if len(s)==1 and s!=" ":
            return 1
        for i in range(len(s)-1,-1,-1):
            if s[i]!=" ":
                count+=1
            if s[i]==" " and i!=len(s)-1 and count!=0 :
                break  
        return count

        """
        :type s: str
        :rtype: int
        """
        