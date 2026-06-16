class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ''

        for st in strs:
            word += str(len(st)) + '#' + st
        
        return word

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while(i < len(s)):
            num = ''
            while(s[i] != '#'):
                num += s[i]
                i += 1
            stop = i + 1
            size = int(num)
            word = ''
            for i in range(stop, stop+size, 1):
                word += s[i]
            i = stop + size
            res.append(word)

        return res

#hello, world -> helloworld -> hello, world
# but str can contain any ascii value.