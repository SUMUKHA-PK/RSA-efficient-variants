import sys
import numpy as np
from math import gcd
from random import randint

MMI = lambda a, n, s=1, t=0, z=0: (n < 2 and t % z or MMI(n, a % n, t, s - a // n * t, z or n), -1)[n < 1]


def generate_message(l):
    return np.array([randint(0, 128) for _ in range(l)])


def is_prime(n, d):

    i = d[-1] + 2
    while i*i <= n:
        prime = True

        for j in d:
            if i % j == 0:
                prime = False
                break

        if prime:
            d.append(prime)

        i += 2

    for j in d:
        if n % j == 0:
            if n == j:
                return True
            else:
                return False

    return True


def generate_primes(n, b):
    primes = []
    bits = int(n/b)
    minimum = 2 ** bits
    maximum = 2 ** (bits+1)

    d = [2, 3, 5, 7]

    for i in range(minimum + 1, maximum):
        if is_prime(i, d):
            primes.append(i)
        if len(primes) >= 2*b:
            break

    primes = np.array(primes)

    if primes.size < b:
        print(primes.size, b)
        print("b is too large. Change b or n")
        sys.exit(-1)

    np.random.shuffle(primes)

    return primes[:b]


def encrypt(message, es, n):
    return [(message[i] ** es[i]) % n for i in range(len(message))]


def main():
    n = int(sys.argv[1])
    b = int(input("Enter b\n"))
    li = int(input("\nEnter l\n"))
    primes = generate_primes(n, b)

    n = np.prod(primes)

    phi_n = 1
    for i in primes:
        phi_n *= (i-1)

    temp = randint(2, 100)
    es = []

    while len(es) < li:
        if gcd(temp, phi_n) == 1:
            is_rp = True
            for i in es:
                if gcd(temp, i) != 1:
                    is_rp = False
                    break
            if is_rp:
                es.append(temp)
        temp += 1

    ds = np.array([MMI(num, phi_n) for num in es])

    d = np.prod(ds)

    # private key
    ds = [(d % p) - 1 for p in primes]

    message = generate_message(li)
    encrypted_message = encrypt(message, es, n)

    print(message, encrypted_message)


if __name__ == '__main__':
    main()
