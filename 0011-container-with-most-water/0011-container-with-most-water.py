class Solution(object):
    def maxArea(self, height):
        x, y = 0, len(height) - 1
        ar = 0
        while x < y:
            d = y - x
            m = min(height[x], height[y])
            ar = max(ar, m * d)
            if height[x] < height[y]:
               x += 1
            else:
                y -= 1
        return ar



        


'''        ar=[0]
        if len(height)>2:
            for m,i in enumerate(height):
                for n,j in enumerate(height):
                    b=abs(m-n)
                    h=min(i,j)
                    y=b*h
                    ar.append(y)
                    ar.remove(min(ar))
            return ar[0]
        else:
            return min(height)'''

       
        
   
        