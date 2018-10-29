import sys
import numpy as np
from math import gcd, log
from random import randint

MMI = lambda a, n, s=1, t=0, z=0: (n < 2 and t % z or MMI(n, a % n, t, s - a // n * t, z or n), -1)[n < 1]


def swap(a, b):
    return b, a


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


def generate_message(l):
    return np.array([randint(0, 128) for _ in range(l)], dtype=object)


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
        print("b is too large. Change b or n")
        sys.exit(-1)

    np.random.shuffle(primes)

    return primes[:b]


def encrypt(message, es, n):
    return [(message[i] ** es[i]) % n for i in range(len(message))]


def interchange(tree):
    for i in range(1, len(tree), 2):
        tree[i], tree[i+1] = swap(tree[i], tree[i+1])


def generate_tree(es):
    leaves = len(es)
    t = int(log(leaves, 2))

    t = 2*(leaves - 2**t)

    tree = [*es[t:], *es[:t]]

    length = 2**(int(log(leaves, 2))+1) + t - 1

    i = len(tree) - 1

    while len(tree) < length:
        tree = [tree[i] * tree[i-1], *tree]
        i -= 1

    interchange(tree)

    return tree


def generate_t(tree):

    i = 0
    t = []
    while 2*i + 2 < len(tree):
        t.append(crt([tree[2*i+1], tree[2*i+2]], [0, 1]))
        i += 1
    return t


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

    # encrypted_messages (Ciphers)
    cs = encrypt(message, es, n)

    # Percolate Up
    e = 1
    for i in es:
        e *= i
    e = e % n

    vs = cs[:]
    v = 1
    # Root node
    for i in range(len(vs)):
        v *= vs[i] ** int((e/es[i]))

    v %= n

    # Exponentiation
    cps = [v % p for p in primes]
    mps = [(cps[i] ** ds[i]) % primes[i] for i in range(len(primes))]

    ys = [int(n/p) for p in primes]
    nis = [ys[i] * MMI(ys[i], primes[i]) for i in range(len(ys))]

    r = 0

    for i in range(len(nis)):
        r += nis[i] * mps[i]

    tree = generate_tree(es)

    ts = generate_t(tree)
    print(ts, tree)


if __name__ == '__main__':
    main()
