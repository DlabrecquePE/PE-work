# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?


def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for x in range(3, int(num ** 0.5) + 1, 2):
        if not num % x:
            return False
    return True


prime_array = []
candidate_value = 2

while len(prime_array) < 10001:
    if is_prime(candidate_value):
        prime_array.append(candidate_value)
    candidate_value += 1

print(prime_array[10000])
