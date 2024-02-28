class Solution:
    def isPalindrome(self, s: str) -> bool:
         
        l=0
        r=len(s)-1
        flag=True
        while l!=r and l<len(s) and r>=0:

            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower()!=s[r].lower():
                    flag=False
                    break
                l+=1
                r-=1
               
            elif s[l].isalnum() and not s[r].isalnum():
                r-=1
            elif not s[l].isalnum() and s[r].isalnum():
                l+=1
            else:
                l+=1
                r-=1

        return flag
            
                

        