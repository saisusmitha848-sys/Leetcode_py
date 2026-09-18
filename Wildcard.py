class Solution:
    def isMatch(self, s, p):
        i = 0
        j = 0

        star = -1
        match = 0

        while i < len(s):

            # Characters match or '?' matches any character
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1

            # Found '*'
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1

            # Mismatch, but we have seen a '*'
            elif star != -1:
                j = star + 1
                match += 1
                i = match

            # Mismatch and no '*'
            else:
                return False

        # Remaining pattern characters must all be '*'
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)