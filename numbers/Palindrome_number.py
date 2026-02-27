def isPalindrome(x):
        last_digit = 0
        original_number = x
        reverse = 0
        while x > 0:
            last_digit = x % 10
            reverse = reverse * 10 + last_digit
            x //= 10
        return original_number == reverse

print(isPalindrome(121))
print(isPalindrome(122))