
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

import time
start_time = time.time()

fibonacci_list = [1, 2]

i = 0
total = 0

while fibonacci_list[i] < 4000000:
    if fibonacci_list[i] % 2 == 0:
        total += fibonacci_list[i]
    fibonacci_list.append(fibonacci_list[i] + fibonacci_list[i+1])
    i += 1
    
print(total)

print("--- %s seconds ---" % (time.time() - start_time))