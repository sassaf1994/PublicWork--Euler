# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import time
start_time = time.time()

test_number = 3
prime_list = [2]

while len(prime_list) < 10002:
    for j in prime_list:
        if test_number % j == 0:
            test_number_status = "NOT PRIME"
            break
        else:
            test_number_status = "PRIME"
    if test_number_status == "PRIME":
        prime_list.append(test_number)
    test_number += 2

print(prime_list[len(prime_list)-1])
        
print("--- %s seconds ---" % (time.time() - start_time))

    