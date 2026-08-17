class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
    
        word1, word2 = list(word1), list(word2)
        start = 0

        word3 = []

        while start < len(word1) and start < len(word2):
            word3.append(word1[start])
            word3.append(word2[start])
            start += 1

        if len(word1) > len(word2):
            word3.extend(word1[start:])

        if len(word2) > len(word1):
            word3.extend(word2[start:])

        return "".join(word3)

'''
word1 = abc, word2 = xyz

word1, word2 = list(word1), list(word2)

start = 0

word3 = []

if not word1:
    word3.extend(word2)

if not word2:
    word3.extend(word1)

while word1 and word2:
    word3.append[start]
    word3.append[word2]
    start += 1

if word1:
    word3.extend(word1)
else:
    word3.extend(word1)

return "".join(word3)

'''