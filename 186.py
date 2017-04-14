# 186 reverse string ii
# Given an input string, reverse the string word by word.
# A word is defined as a sequence of non-space characters.
# 
# The input string does not contain leading or trailing spaces
# and the words are always separated by a single space.
# 
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
# 
# Could you do it in-place without allocating extra space?
#

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: str
        """
        
        # s.reverse()
        self.rw(s, 0, len(s))
        print s
        l=0
        for i in range(len(s)):
            if s[i] == ' ':
                self.rw(s, l, i)
                l=i+1
            if i == len(s)-1:
                self.rw(s, l, len(s))
                
    def rw(self, s, l, i):
        while l< i-1:
            temp = s[l]
            s[l]=s[i-1]
            s[i-1]=temp
            l+=1
            i-=1

if __name__ == '__main__':
    s= ["a", "b", " ", "c", "d"]
    Solution().reverseWords(s)
    print s