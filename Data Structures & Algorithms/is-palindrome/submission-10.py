class Solution:
    def isPalindrome(self, s: str) -> bool:

        def checker(char):
            if (ord(char) < 48 or ord(char) > 57) and (ord(char) < 65 or ord(char) > 90) and (ord(char) < 97 or ord(char) > 122):
                return False
            return True

        s = s.lower()
        s = s.replace(" ", "")

        start = 0
        end = len(s)-1

        while start < end:
            print(s[start])
            while not checker(s[start]) and start < end:
                start += 1
            while not checker(s[end]) and start < end:
                end -= 1
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True