if n ==1:
            return 1
        if n ==2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)

        class Solution(object):
    

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n ==1 or n==2:
            return n
      
            
        a= [1]*n
        a[1]=2
        
        for i in range (2,n):
            a[i]=a[i-1]+a[i-2]
        
        return a[n-1]






        def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n ==1 or n==2:
            return n
      
            
        a = 1
        b = 2
        result =0
        
        for i in range(n-2):
            result = a+b
            a =b
            b = result
            
        
        return result