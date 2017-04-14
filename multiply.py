class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 =0
        for n in num1:
            n1= n1*10+int(n)
        
        n2 =0
        for n in num2:
            n2= n2*10+int(n)
        nbig = n1*n2
        
        return str(nbig)

        # nbig = int(num1)*int(num2)
        
        # return str(nbig)