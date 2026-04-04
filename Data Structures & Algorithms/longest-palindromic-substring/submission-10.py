class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def ispalindrome(s):
            l = 0
            r = len(s)-1
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        if ispalindrome(s):
            return s
        substrings = []
        for i in range(len(s)-1):
            for j in range(i,len(s)):
                substrings.append(s[i:j+1])
        maxcount = 0
        lgsubstring = ""
        for substring in substrings:
            if ispalindrome(substring):
                if maxcount < len(substring):
                    maxcount = len(substring)
                    lgsubstring = substring
        return lgsubstring
        