class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        otp = 0
        tmp = 0

        for c in s:
            val = mapping.get(c)

            # roman numerals are usually written largest to smallest (XXVII)
            # detect subtraction (IV)
            if tmp < val:
                # subtract from value and otp
                tmp = val - (tmp * 2)
            else:
                # add w/o change
                tmp = val
                
            otp += tmp

        return otp


# given
x = ["III", "IV", "IX", "LVIII", "MCMXCIV"]

# debug
for i in range(len(x)):
    print(x[i], Solution().romanToInt(x[i]))