# Sum square difference
# Problem 6
# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is
# 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.


n = 100
squares_of_naturals = [i ** 2 for i in range(1, n + 1)]
sum_of_naturals = n * (n + 1) // 2              # arithemetic progression

print(sum_of_naturals ** 2 - sum(squares_of_naturals))
