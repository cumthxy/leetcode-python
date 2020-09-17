
class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=""
        for i in range(len(s)):
            if s[i].isalnum():
                result = result+s[i].lower()


        reverse_result = result[::-1]
        print(result)
        print(reverse_result)
        if result==reverse_result:
            return True
        else:
            return False

s = Solution()
s.isPalindrome( "A man, a plan, a canal: Panama")



