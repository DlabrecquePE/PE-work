# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

factorize_this = 600851475143


def gen_primes():
    """ Generate an infinite sequence of prime numbers """
    d, q = {}, 2
    while True:
        if q not in d:
            yield q
            d[q * q] = [q]
        else:
            for p in d[q]:
                d.setdefault(p + q, []).append(p)
            del d[q]
        q += 1


def factorize(num, primes=gen_primes()):
    """ Returns a list of prime factors of num """
    if not float(num).is_integer() or num < 1:
        raise Exception("Error: Can only factorize positive integers.")
    prime_factors = []
    for prime in primes:
        while not num % prime:
            prime_factors.append(prime)
            num = num // prime
        if num == 1:
            return prime_factors


res = factorize(factorize_this)
print(max(res))
