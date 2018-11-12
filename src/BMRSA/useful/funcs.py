import numpy as np
import sys
from random import randint
from math import gcd

MMI = lambda a, n, s=1, t=0, z=0: (n < 2 and t % z or MMI(n, a % n, t, s - a // n * t, z or n), -1)[n < 1]


# function implementing Chinese remainder theorem
# list m contains all the modulus
# list x contains the remainders of the equations
def crt(m, x):
    # We run this loop while the list of
    # remainders has length greater than 1
    while True:

        # temp1 will contain the new value
        # of A. which is calculated according
        # to the equation m1' * m1 * x0 + m0'
        # * m0 * x1
        temp1 = MMI(m[1], m[0]) * x[0] * m[1] + \
                MMI(m[0], m[1]) * x[1] * m[0]

        # temp2 contains the value of the modulus
        # in the new equation, which will be the
        # product of the modulus of the two
        # equations that we are combining
        temp2 = m[0] * m[1]

        # we then remove the first two elements
        # from the list of remainders, and replace
        # it with the remainder value, which will
        # be temp1 % temp2
        x.remove(x[0])
        x.remove(x[0])
        x = [temp1 % temp2] + x

        # we then remove the first two values from
        # the list of modulus as we no longer require
        # them and simply replace them with the new
        # modulus that  we calculated
        m.remove(m[0])
        m.remove(m[0])
        m = [temp2] + m

        # once the list has only one element left,
        # we can break as it will only  contain
        # the value of our final remainder
        if len(x) == 1:
            break

    # returns the remainder of the final equation
    return x[0]


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


def swap(a, b):
    return b, a


def generate_message(l, n):
    return np.array([randint(1, min(128, n)) for _ in range(l)], dtype=object)


def es(ps, li):
    phi = 1
    for ii in ps:
        phi *= (ii - 1)

    temp = randint(2, 100)
    ess = []

    while len(ess) < li:
        if gcd(temp, phi) == 1:
            is_rp = True
            for ii in ess:
                if gcd(temp, ii) != 1:
                    is_rp = False
                    break
            if is_rp:
                ess.append(temp)
        temp += 1

    return ess
