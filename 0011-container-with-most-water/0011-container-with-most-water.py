class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        Max = 0
        while left < right:
            d = right - left
            m = min(height[left], height[right])
            Max = max(Max, m * d)
            if height[left] < height[right]:
               left += 1
            else:
                right -= 1
        return Max

'''        x,y=0,len(height)-1
        ar=[0]
        while True:
            if y>x:
               b=y-x
               h=min(height[x],height[y])
               ar.append(h)
               ar.remove(min(ar))
               x+=1
               y-=1
            else:
                x=len(height)
        
        return ar[0]'''

        


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

       
        
   
        