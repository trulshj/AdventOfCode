from math import sqrt, ceil
from functools import cache
from time import time


start_time = time()


def is_prime(n):
    if n < 2:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    limit = ceil(sqrt(n)) + 1

    for i in range(2, limit):
        if n % i == 0:
            return False
    return True


def fast_primes(n):
    """Computes all primes up to n using the Sieve of Eratosthenes"""
    if n < 2:
        return []

    prime_cache = [2]

    if n == 2:
        return prime_cache

    for i in range(3, n+1, 2):
        limit = ceil(sqrt(i)) + 1
        for p in prime_cache:
            if p > limit:
                prime_cache.append(i)
                break

            if i % p == 0:
                break
        else:
            prime_cache.append(i)

    return prime_cache


SIEVE_SIZE = 10_000_000
# primes = [i for i in range(2, 10_000_000) if is_prime(i)]
primes = fast_primes(SIEVE_SIZE)
sieve = [True] * SIEVE_SIZE

# for prime in primes:
#     i = prime - 1
#     while i < len(sieve)-1:
#         sieve[i] = False
#         i += prime
#     print(prime, sum(sieve) / len(sieve))


@cache
def f(n):
    if n == 0:
        return 1

    return f(n-1) * (1 - (1/primes[n-1]))


@cache
def g(n):
    result = 1
    for i in range(n):
        result *= (1 - 1 / primes[i])
    return result


for i in range(1, len(primes)+1):
    print(f"n: {i}, p_n: {primes[i-1]}, remainder: {f(i)}")


print("Execution time:", time() - start_time)
