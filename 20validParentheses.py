class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        a=[]
        for i in s:
            if i==')':
                if len(a)==0:
                    return False
                if a[-1]=='(':
                    del a[-1]
                else:
                    return False
            elif i==']':
                if len(a)==0:
                    return False
                if a[-1]=='[':
                    del a[-1]
                else:
                    return False 
            elif i=='}':
                if len(a)==0:
                    return False
                if a[-1]=='{':
                    del a[-1]
                else:
                    return False
            else:
                a.append(i)
        if len(a)==0:
            return True
        else:
            return False
