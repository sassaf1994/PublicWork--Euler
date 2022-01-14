# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import time
start_time = time.time()

dict_of_primes = {}

def prime_factorisation(number):
    prime_number_divisor = 2
    list_of_primes = []
    while number > 1:
        if number % prime_number_divisor == 0:
            number = number / prime_number_divisor
            list_of_primes.append(prime_number_divisor)
        else:
            prime_number_divisor += 1
    return list_of_primes


for number in range(21):
    prime_list = prime_factorisation(number)
    for i in prime_list:
        try:
            if prime_list.count(i) > dict_of_primes[i]:
                dict_of_primes[i] = 0
                dict_of_primes[i] = dict_of_primes.get(i, 0) + prime_list.count(i)
            else: 
                continue
        except:
            dict_of_primes[i] = dict_of_primes.get(i, 0) + 1
            
print(dict_of_primes)   
total = 1

for i in dict_of_primes:
    total = total * int(i) ** int(dict_of_primes[i])

print("The lowest number which is a multiple of all digits from 1 - 20 is:",total)

print("--- %s seconds ---" % (time.time() - start_time))
