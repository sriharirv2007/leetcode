class Solution(object):
    def angleClock(self, hour, minutes):
        am=6*minutes
        ah=(hour*30)+(0.5*minutes)
        a=abs(am-ah)
        return min(a,360-a)


        
    
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        