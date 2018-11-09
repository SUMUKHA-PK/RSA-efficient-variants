import sys
import numpy as np
from math import gcd
from random import randint
sys.path.append((os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))))
from crt import crt

MMI = lambda a, n, s=1, t=0, z=0: (n < 2 and t % z or MMI(n, a % n, t, s - a // n * t, z or n), -1)[n < 1]


def swap(a, b):
    return b, a

def generate_message(m):
    return randint(0, min(m, 128))


def is_prime(n, d):

    i = d[-1] + 2
    while i*i <= n:
        prime = True

        for j in d:
            if i % j == 0:
                prime = False
                break

        if prime:
            d.append(i)

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
    minimum = 2 ** (bits-1)
    maximum = 2 ** bits

    d = [2, 3, 5, 7]

    for i in range(minimum + 1, maximum):
        if is_prime(i, d):
            primes.append(i)

        if len(primes) >= 2*b:
            break

    primes = np.array(primes, dtype=object)

    if primes.size < b:
        print("b is too large. Change b or n")
        sys.exit(-1)

    np.random.shuffle(primes)

    return primes[:b]


def encrypt_decrypt(message, e, n):
    return (message ** e) % n


def main():
    n = int(sys.argv[1])
    b = int(input("Enter b\n"))
    primes = generate_primes(n, b)

    n = np.prod(primes)

    phi_n = 1
    for i in primes:
        phi_n *= (i-1)

    temp = randint(2, min(100, phi_n - 1))

    while True:
        is_rp = False
        if gcd(temp, phi_n) == 1:
            is_rp = True
        if is_rp:
            break
        temp += 1

    e = temp

    d = MMI(e, phi_n) % phi_n

    # private key
    # Check
    message = generate_message(n)

    # encrypted_messages (Ciphers)
    c = encrypt_decrypt(message, e, n)

    # decryption
    de = encrypt_decrypt(c, d, n)

    print("message      : ", message)
    print("cipher       : ", c)
    print("decrypted    : ", de)

    if message == de:
        print("CORRECT")


if __name__ == '__main__':
    main()
