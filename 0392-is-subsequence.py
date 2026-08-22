#inefficient way: compare s1 to t1, t2, ..., tk where k=len(t); repeat for s2, ..., sn where n=len(s)

class Solution:
    def isSubsequence(self, s, t, x=0, y=0):
        #0
        if len(s)==0 and len(t)==0:
            return True
        #0.1
        if len(s)==0 and len(t)!=0:
            return True
        #0.2
        if len(s)!=0 and len(t)==0:
            return False
        #1
        if x==len(s)-1 and y==len(t) - 1 and s[x]!=t[y]:
            return False
        #2
        if x==len(s)-1 and y==len(t) - 1 and s[x]==t[y]:
            return True
        #3
        if x==len(s)-1 and y!=len(t)-1 and s[x]==t[y]:
            return True
        #4
        if x==len(s)-1 and y!=len(t)-1 and s[x]!=t[y]:
            return self.isSubsequence(s, t, x, (y+1))
        #5
        if x!=len(s)-1 and y==len(t)-1 and s[x]!=t[y]:
            return False
        #6
        if x!=len(s)-1 and y==len(t)-1 and s[x]==t[y]:
            return False
        #7
        if x!=len(s)-1 and y!=len(t)-1 and s[x]!=t[y]:
            return self.isSubsequence(s, t, x, (y+1))
        #8
        if x!=len(s)-1 and y!=len(t)-1 and s[x]==t[y]:
            return self.isSubsequence(s, t, (x+1), (y+1))

solution = Solution()
print(solution.isSubsequence("aza", "abzba"))

# different scenarios:
# s is at the end, t is at the end, s does not equal t ==> false

# s is at the end, t is at the end, s does equal t ==> true

# s is at the end, t is not at the end, s does equal t ==> true

# s is at the end, t is not at the end, s does not equal t ==> add 1 to t

# s is not at the end, t is at the end, s does not equal t ==> false

# s is not at the end, t is at the end, s does equal t ==> false

# s is not at the end, t is not at the end, s does not equal t ==> add 1 to t

# s is not at the end, t is not at the end, s does equal t ==> add 1 to s and t

