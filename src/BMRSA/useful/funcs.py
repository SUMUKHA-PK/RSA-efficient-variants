import numpy as np
import sys
from random import randint
from math import gcd

# function to find the modulo inverse of a number mod n
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


# function to find if a number n is prime looking at dictionary of primes d
def is_prime(n, d):

    # generating primes till n
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

    # checking if any of primes divide n
    for j in d:
        if n % j == 0:
            # if n is itself a prime
            if n == j:
                return True
            else:
                return False

    #  n is prime
    return True


# generating b primes of n/b bits
def generate_primes(n, b):

    # initially no primes present
    primes = []
    bits = int(n/b)

    # start from the first number which is n/b bits long
    minimum = 2 ** (bits-1)

    # till last number n/b bits long
    maximum = 2 ** bits

    # basic dictionary
    d = [2, 3, 5, 7]

    # finding if any of the number is prime and stopping if more than 2*b primes are acquired
    for i in range(minimum + 1, maximum):
        if is_prime(i, d):
            primes.append(i)
        if len(primes) >= 2*b:
            break

    primes = np.array(primes, dtype=object)

    # if less than b primes present then stop
    if primes.size < b:
        print("b is too large. Change b or n")
        sys.exit(-1)

    # randomise primes and select first b of it
    np.random.shuffle(primes)

    return primes[:b]


# swap two numbers
def swap(a, b):
    return b, a


# Generate message of of length l
def generate_message(l, n):
    return np.array([randint(1, min(128, n)) for _ in range(l)], dtype=object)


#  Generate es which are co-prime to phi and themselves
def es(ps, li):

    # phi value is (p1-1)*(p2-1)*....(pn-1)
    phi = 1
    for ii in ps:
        phi *= (ii - 1)

    # start from a random value
    temp = randint(2, 5)
    ess = []

    # finding numbers co prime to and themselves
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

    # return array of co primes to phi
    return ess
