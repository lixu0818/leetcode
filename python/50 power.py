class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0 or x==1:
            return 1
            
        invert = False
        if n <0 and x*x<1:
            n=-1
            x= 1.0/x
        elif n<0:
            n=-1
            invert = True
        elif x*x<1:
            x=1.0/x
            invert = True
            
       
        result = 1
        for i in range(n):
            result *= x
            
        if result > float("inf"):
            result = float("inf")
        if result < float("-inf"):
            result = float("-inf")  
        if invert:
            result = 1.0/float("inf")
        return result    
            

            class Solution:
    def myPow(self, x, n):
        if n==0:
            return 1
        if n<0:
            return 1.0/self.myPow(x,-n)
        elif n%2 !=0:
            return x*self.myPow(x, n-1)
        else:
            return self.myPow(x*x, n/2)