# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_of_square = 0
square_of_sum = [i for i in range(101)]

for i in range(101):
    sum_of_square = sum_of_square + i ** 2

print(sum(square_of_sum) ** 2 - sum_of_square)