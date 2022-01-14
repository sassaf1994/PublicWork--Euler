# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

import time
start_time = time.time()

num = 999 * 999
palindrome_numbers = []
three_digit_numbers = [x for x in range(100,1000)]


while num > 100 * 100:
    palindrome_string = [int(i) for i in str(num)]
    palindrome_string_rev = list(reversed(palindrome_string))
    if palindrome_string == palindrome_string_rev:
        palindrome_numbers.append(num)
    num -= 1

palindromic_numbers_multiples_of_two_integers = []

def isfactor(x):
    for i in three_digit_numbers:
        if x % i == 0:
            n = x / i
            if 10 <= n < 1000:
                palindromic_numbers_multiples_of_two_integers.append(x)
                break

for palindrome in palindrome_numbers:
    isfactor(palindrome)
    
print(palindromic_numbers_multiples_of_two_integers[0])

print("--- %s seconds ---" % (time.time() - start_time))
