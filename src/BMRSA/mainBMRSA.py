import numpy as np
from math import gcd, log
from random import randint
import sys
import time
from useful import funcs


def encrypt(message, es, n):
    return [(message[i] ** es[i]) % n for i in range(len(message))]


def generate_tree_e(es, n):
    leaves = len(es)
    t = int(log(leaves, 2))

    t = 2*(leaves - 2**t)

    tree = [*es[t:], *es[:t]]

    length = 2**(int(log(leaves, 2))+1) + t - 1

    i = len(tree) - 1

    while len(tree) < length:
        tree = [tree[i] * tree[i-1] % n, *tree]
        i -= 1

    return tree


def generate_tree_v(vs, tree_es, n):
    leaves = len(vs)
    t = int(log(leaves, 2))

    t = 2 * (leaves - 2 ** t)

    tree = [*vs[t:], *vs[:t]]

    length = 2 ** (int(log(leaves, 2)) + 1) + t - 1

    tree = [*[0 for _ in range(length - len(tree))], *tree]

    i = len(tree) - len(vs) - 1

    while i >= 0:
        left = 2*i + 1
        right = 2*i + 2
        tree[i] = ((tree[left]**tree_es[right])*(tree[right]**tree_es[left])) % n
        i -= 1

    return tree


def generate_r(tree_es, tree_vs, n, r):
    n = int(n)

    i = 0
    tree = [r, *[0 for _ in range(len(tree_vs)-1)]]

    while 2*i + 2 < len(tree):
        r = tree[i]
        left = 2*i + 1
        right = 2*i + 2
        t = funcs.crt([tree_es[left], tree_es[right]], [0, 1])
        t_l = int(t//tree_es[left])
        t_r = int((t-1)//tree_es[right])
        r_r = (tree[i]**t)*funcs.MMI((tree_vs[right]**t_r)*(tree_vs[left]**t_l), n) % n
        r_l = (r*(MMI(r_r, n))) % n
        tree[left] = r_l
        tree[right] = r_r
        i += 1

    return tree


def main(primes, es):

    ds = np.array([funcs.MMI(num, phi) for num in es], dtype=object)

    d = np.prod(ds) % phi

    # private key
    ds = [d % (p - 1) for p in primes]

    message = funcs.generate_message(li)

    # encrypted_messages (Ciphers)
    cs = encrypt(message, es, no)

    vs = cs[:]

    tree_es = generate_tree_e(es, phi)

    tree_vs = generate_tree_v(vs, tree_es, no)

    v = tree_vs[0]

    # Exponentiation
    cps = [v % p for p in primes]
    mps = [(cps[i] ** ds[i]) % primes[i] for i in range(len(primes))]

    ys = [no // p for p in primes]
    nis = [ys[i] * funcs.MMI(ys[i], primes[i]) for i in range(len(ys))]

    r = 0

    for i in range(len(nis)):
        r += nis[i] * mps[i]

    r %= no

    r = int(r)

    print(tree_vs, tree_es)

    start = time.clock()

    tree_rs = generate_r(tree_es, tree_vs, no, r)

    end = time.clock() - start

    _ = tree_rs

    # decrypted = tree_rs[-li:]
    #
    # t = int(log(li, 2))
    #
    # t = 2 * (li - 2 ** t)
    #
    # decrypted = [*decrypted[li - t:], *decrypted[0: li - t]]
    #
    # print(tree_rs, n)
    #
    # print("decrypted :", decrypted)

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

    print(main(ps, ess))
