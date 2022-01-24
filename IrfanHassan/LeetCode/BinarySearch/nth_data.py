class Solution:
    def findNthDigit(self, n):
        l = 0
        while n > (9 * 10**l)*(l+1):
            n -= (9 * 10 ** l)*(l+1)
            l += 1
        number_of_digits = (l+1)
        digit_to_check = (10**l)+((n-1)//number_of_digits)
        digit_from_left = (n-1)%number_of_digits
        digit_position = list(str(digit_to_check))
        return digit_position[digit_from_left]