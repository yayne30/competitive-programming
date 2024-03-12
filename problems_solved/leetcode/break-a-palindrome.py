class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        leng = len(palindrome)
        ans = ''
        if leng == 1:
            return ""
        for i in range(leng):
            if leng % 2 == 0:
                if palindrome[i] != "a":
                    ans += 'a'
                    ans += palindrome[i + 1:]
                    break
                elif palindrome[i] == 'a' and i == leng - 1:
                    ans += 'b'
                else:
                    ans += palindrome[i]
            else:
              
                if palindrome[i] != "a" and i != (leng // 2):
                    ans += 'a'
                    ans += palindrome[i + 1:]
                    break
                elif palindrome[i] == 'a' and i == leng - 1:
                    print(1)
                    ans += 'b'
                else:
                    ans += palindrome[i]
        return ans





        # s=list(palindrome.split())
        # if len(s)==1:
        #     return ""
        # else:
        #     if len(set(s))==1 and s[0]=='a':
        #         s[len(s)-1]='b'
        #     p=len(s)//2
        #     print (p)
        #     for i in range(p):
        #         print (s[i])
        #         if s[i]!='a':
        #             s[i]='a'
        #             break
        # return s.join() 
            



            
        
        