class Solution(object):
    def largestAltitude(self, gain):
        y=0
        al=[]
        for i in range(0,len(gain)):
            y=y+gain[i]
            al.append(y)
        if max(al)>=0:
            return max(al)
        else:
            return 0
            





            

        """
        :type gain: List[int]
        :rtype: int
        """
        