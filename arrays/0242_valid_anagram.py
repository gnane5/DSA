class Solution(object):
    def isAnagram(self, s, t):
        c=dict()
        o=dict()
        for i in s:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        
        for i in t:
            if i in o:
                o[i]+=1
            else:
                o[i]=1

        if c==o:
            return True
        else:
            return False