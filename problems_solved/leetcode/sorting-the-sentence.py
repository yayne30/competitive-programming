class Solution:
    def sortSentence(self, s: str) -> str:

        s_splited = s.split(' ')
        ans = ''
        s_splited.sort(key = lambda x : x[-1])
        cnt = Counter(s)

    
        for i in s_splited:
            
            print()
            ans += i[:-1]
            if int(i[-1]) < len(s_splited):
                ans += ' '
        return ans


        
        # cnt = Counter(s)
        # str_array= [''] *( cnt[' '] + 2)
        # temp = ''
        # ans = ''

        # for i in s:
        #     if not i.isdigit() and i != ' ':
        #         temp += i
        #     elif i.isdigit():
        #         str_array[int(i)]= temp
        #         temp = ''

        # for i in range( 1, len(str_array)):
        #     ans += str_array[i]
        #     if i != len(str_array) - 1:
        #         ans += ' '

        # return ans
        