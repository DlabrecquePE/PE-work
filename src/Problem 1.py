# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

n = 999

res = n // 3 * 1002 + n // 5 * 1000 - n // 15 * 1005
print(res // 2)
