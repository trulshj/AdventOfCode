from math import sqrt, ceil, gcd, lcm
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


SIEVE_SIZE = 1_000
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


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator
        
    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        divisor = gcd(numerator, denominator)
        return Fraction(numerator // divisor, denominator // divisor)
    
    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        divisor = gcd(numerator, denominator)
        return Fraction(numerator // divisor, denominator // divisor)
    
    def __sub__(self, other):
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        divisor = gcd(numerator, denominator)
        return Fraction(numerator // divisor, denominator // divisor)
    
    def decimal(self):
        return self.numerator / self.denominator


def calculate_fraction(primes: list[int]):
    result = Fraction(1, 1)
    for i in range(len(primes)):
        result *= Fraction(primes[i] - 1, primes[i])
        yield result
    


# for i in range(1, len(primes)+1):
#     print(f"n: {i}, p_n: {primes[i-1]}, remainder: {f(i)}")

for i, fraction in enumerate(calculate_fraction(primes), 1):
    print(f"n: {i}, fraction: {fraction}, decimal: {fraction.decimal()}")

print("Execution time:", time() - start_time, "seconds")
