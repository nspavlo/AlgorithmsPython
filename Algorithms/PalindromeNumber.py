class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = x
        reverseNumber = 0

        while number > 0:
            # calculate last digit (23 -> 3)
            digit = number % 10

            # append last digit to reverseNumber (0 + 3 -> 3), (3 + 2 -> 32)
            reverseNumber = (reverseNumber * 10) + digit

            # remove last digit from number (1.2 -> 1)
            number = int(number / 10)

        return reverseNumber == x


# given
x = [121, -121, 10, -101, 101, 10000000000001, 0]

# debug
for i in range(len(x)):
    print(x[i], Solution().isPalindrome(x[i]))