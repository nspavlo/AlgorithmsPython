class Solution:
    def reverse(self, x: int) -> int:
        i = str(abs(x))
        j = int(i[::-1])

        # limit to 32 bit integer
        if j > 0x7FFFFFFF:
            return 0

        if x < 0:
            return j * -1
        else:
            return j


# given
x = 1534236469

# debug 9646324351
print(Solution().reverse(x))