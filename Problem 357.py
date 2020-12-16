from collections import deque


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


def pfactor(num, p):
    """ Returns a dict of prime factors of num          """
    """ dict keys are the prime factors                 """
    """ values contain the number of factors (exponent) """

    prime_factors = {}
    for prime in p:
        while not num % prime:
            prime_factors[prime] = prime_factors.get(prime, 0) + 1
            num = num // prime
        if num == 1:
            return prime_factors
        if prime > num ** 0.5:
            prime_factors[num] = 1
            return prime_factors


def divisors(num, p):
    """ takes a dict of prime factors from pfactor()    """
    """ returns list of divisors                        """

    num_dict = pfactor(num, p)

    def inner_divisors(num_dict, num_list={1}):
        if not num_dict:
            return num_list

        prime = min(num_dict.keys())
        exp = num_dict[prime]
        del num_dict[prime]
        back_list = inner_divisors(num_dict, num_list)
        work_list = [prime ** (i + 1) for i in range(exp)]
        for div in work_list:
            num_list = num_list.union(x * div for x in back_list)
        num_list = num_list.union(work_list).union(back_list)
        return num_list

    return sorted(list(inner_divisors(num_dict))[1: -1])


from time import time

start = time()
max_n, primer, res = 10 ** 8, gen_primes(), 0
prime = next(primer)
pri_list = {prime}
while True:
    prime = next(primer)
    pri_list.add(prime)
    n = prime - 1
    if n > max_n:
        break
    div = deque(divisors(n, pri_list))
    while len(div) not in [0, 1]:
        if div.pop() + div.popleft() not in pri_list:
            break
        if not div:
            res += n

print(res + 3, time() - start)
