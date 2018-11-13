import sys
import numpy as np
from math import gcd, inf
from random import randint
import time
from useful import funcs


# standard message encryption = m ** e mod N
def encrypt_decrypt(message, e, n):
    return (message ** e) % n


# Driver function
def main(primes, e, message):
    # Start timer
    start = time.clock()

    # N = p1*p2....
    n = np.prod(primes)

    # phi = (p1 - 1)*(p2 - 2)....
    phi_n = 1
    for i in primes:
        phi_n *= (i - 1)

    # Find MMI(e, phi_n)
    d = funcs.MMI(e, phi_n) % phi_n

    # encrypted_messages (Ciphers)
    c = encrypt_decrypt(message, e, n)

    # decryption
    de = encrypt_decrypt(c, d, n)

    # decrypted message
    if message == de:
        return time.clock() - start

    return inf


# Test function only
# Run only from main driver
if __name__ == '__main__':
    no = int(sys.argv[1])
    b = int(input("Enter b\n"))
    ps = funcs.generate_primes(no, b)

    phi = 1
    for ii in ps:
        phi *= (ii - 1)

    temp = randint(2, min(100, phi - 1))

    while True:
        is_rp = False
        if gcd(temp, phi) == 1:
            is_rp = True
        if is_rp:
            break
        temp += 1

    print(main(ps, temp, funcs.generate_message(n)))
