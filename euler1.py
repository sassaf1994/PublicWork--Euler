# Find the sum of all the multiples of 3 or 5 below 1000.

total1 = 0
for e in range(1000):
    if e % 5 == 0 or e % 3 == 0:
        total1 += e

print(total1)