import numpy as np
from math import gcd, log
from random import randint
import sys
import time
from useful import funcs


# standard message encryption = m ** e mod N
def encrypt(message, es, n):
    return [(message[i] ** es[i]) % n for i in range(len(message))]


#  PERCOLATE UP

# 1. Generate tree of all co prime factors i.e used to find modulo inverse of es
def generate_tree_e(es, phi):

    #  creating a full binary tress
    leaves = len(es)
    t = int(log(leaves, 2))

    t = 2*(leaves - 2**t)

    tree = [*es[t:], *es[:t]]

    length = 2**(int(log(leaves, 2))+1) + t - 1

    i = len(tree) - 1

    # e = er * el % phi
    while len(tree) < length:
        tree = [tree[i] * tree[i-1] % phi, *tree]
        i -= 1

    return tree


# 2. Generate cipher tree
def generate_tree_v(vs, tree_es, n):

    # Full binary tree
    leaves = len(vs)
    t = int(log(leaves, 2))

    t = 2 * (leaves - 2 ** t)

    tree = [*vs[t:], *vs[:t]]

    length = 2 ** (int(log(leaves, 2)) + 1) + t - 1

    tree = [*[0 for _ in range(length - len(tree))], *tree]

    i = len(tree) - len(vs) - 1

    # v =   vL ** er * vR ** el % n
    while i >= 0:
        left = 2*i + 1
        right = 2*i + 2
        tree[i] = ((tree[left]**tree_es[right])*(tree[right]**tree_es[left])) % n
        i -= 1

    return tree


# PERCOLATE DOWN
# Generate root tree to find messages in leaves
def generate_r(tree_es, tree_vs, n, r):
    n = int(n)

    # Full binary tree
    i = 0
    tree = [r, *[0 for _ in range(len(tree_vs)-1)]]

    # Algorithm wrong in paper
    # t = 0 mod El and t = 1 mod ER and solving t using crt
    # rR = r**t / vL ** tL * vR ** tr % n
    while 2*i + 2 < len(tree):
        r = tree[i]
        left = 2*i + 1
        right = 2*i + 2
        t = funcs.crt([tree_es[left], tree_es[right]], [0, 1])
        t_l = int(t//tree_es[left])
        t_r = int((t-1)//tree_es[right])
        r_r = (tree[i]**t)*funcs.MMI((tree_vs[right]**t_r)*(tree_vs[left]**t_l), n) % n
        r_l = (r*(funcs.MMI(r_r, n))) % n
        tree[left] = r_l
        tree[right] = r_r
        i += 1

    return tree


# Testing function
# Run only from main driver
def main(primes, es, message):

    phi = 1
    n = 1

    for p in primes:
        phi *= (p-1)

    for p in primes:
        n *= p

    ds = np.array([funcs.MMI(num, phi) for num in es], dtype=object)

    d = np.prod(ds) % phi

    # private key
    ds = [d % (p - 1) for p in primes]

    # encrypted_messages (Ciphers)
    cs = encrypt(message, es, n)

    vs = cs[:]

    tree_es = generate_tree_e(es, phi)

    tree_vs = generate_tree_v(vs, tree_es, n)

    v = tree_vs[0]

    # Exponentiation
    cps = [v % p for p in primes]
    mps = [(cps[i] ** ds[i]) % primes[i] for i in range(len(primes))]

    ys = [n // p for p in primes]
    nis = [ys[i] * funcs.MMI(ys[i], primes[i]) for i in range(len(ys))]

    r = 0

    for i in range(len(nis)):
        r += nis[i] * mps[i]

    r %= n

    r = int(r)

    start = time.clock()

    tree_rs = generate_r(tree_es, tree_vs, n, r)

    end = time.clock() - start

    _ = tree_rs

    return end


if __name__ == '__main__':
    if len(sys.argv) > 1:
        no = int(sys.argv[1])
    else:
        no = 10

    bb = int(input("Enter b\n"))
    li = int(input("\nEnter l\n"))
    ps = funcs.generate_primes(no, bb)

    no = np.prod(ps)

    m = funcs.generate_message(li)

    print(main(ps, ess, m))
