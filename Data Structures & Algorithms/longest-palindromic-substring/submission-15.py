class Solution:
    def longestPalindrome(self, s: str) -> str:
        # every character in itself is a palindrome. start with each character, then expand out from both sides. 
        lgsubstring = ""
        maxcount = 1
        n = len(s)
        for i in range(n):
            l = i
            r = i
            while l>=0 and r<n and s[l] == s[r]:
                l-=1
                r+=1
            if maxcount <= r-l-1:
                lgsubstring = s[l+1:r]
                maxcount = r-l-1
            l,r = i, i+1
            while l>=0 and r<n and s[l] == s[r]:
                l-=1
                r+=1
            if maxcount <= r-l-1:
                lgsubstring = s[l+1:r]
                maxcount = r-l-1
                
        return lgsubstring


            


        