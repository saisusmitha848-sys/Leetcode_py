class Solution:
    def myAtoi(self, s):
        s = s.strip()
        sign = 1
        i = 0
        num = 0

        if s and s[0] in "+-":
            if s[0] == "-":
                sign = -1
            i += 1

        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num *= sign

        return max(-2**31, min(num, 2**31 - 1))