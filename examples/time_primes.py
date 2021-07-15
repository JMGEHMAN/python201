import concurrent.futures
import math
import timeit

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def parallel():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            pass


def serial():
    for prime in PRIMES:
        is_prime(prime)

if __name__ == '__main__':
    # Note the two ways to get the functions into the namespace...
    print(timeit.repeat(stmt="parallel()", number=1, repeat=3, globals=globals()))
    print(timeit.repeat("serial()", number=1, repeat=3, setup="from __main__ import serial"))