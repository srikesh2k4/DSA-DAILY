class Solution(object):
    def reverseVowels(self, s):
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        i = 0
        j = len(s)-1
        rev = list(s)
        while(i<j):
            if(s[i] in vowel and s[j] in vowel):
                rev[i],rev[j] = rev[j],rev[i]
                i += 1
                j -= 1
            elif(s[i] in vowel and s[j] not in vowel):
                j -= 1
            elif(s[i] not in vowel and s[j] in vowel):
                i += 1
            elif(s[i] not in vowel and s[j] not in vowel):
                i += 1
                j -= 1
        return ''.join(rev)

            

        