# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 

import time
start_time = time.time()

prime = 2
number = 600851475143
a = []

while number > 1:
    if number % prime == 0:
        number = number / prime
        a.append(prime)
    else:
        prime += 1

print(a[len(a)-1])

print("--- %s seconds ---" % (time.time() - start_time))