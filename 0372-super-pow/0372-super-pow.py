class Solution(object):
    def superPow(self, a, b):
        n=0
        for i in range(0,len(b)):
            if b[i]==0:
                n*=10
            else:
                n=n*10+b[i]
        return pow(a, n, 1337)

      