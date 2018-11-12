import mainBMRSA as Bmrsa
import mainMRSA as Mrsa
import matplotlib.pyplot as plt

from useful import funcs

bsize = 1

while bsize < 4:
    itr = 10
    mrsa = []
    bmrsa = []
    pts = []
    while itr <= 18:

        pts.append(2 ** itr)

        n = itr
        b = 2
        ll = bsize

        primes = funcs.generate_primes(n, b)

        n = 1

        for p in primes:
            n *= p

        m = funcs.generate_message(ll, n)

        es = funcs.es(primes, ll)

        timeMRSA = 0

        for i in range(ll):
            timeMRSA += Mrsa.main(primes, es[i], m[i])

        mrsa.append(timeMRSA*1000)

        timeBMRSA = Bmrsa.main(primes, es, m)

        bmrsa.append(timeBMRSA*1000)

        itr += 2

    fig, ax = plt.subplots()
    ax.plot(pts, mrsa, "ro-", label="MRSA")
    ax.plot(pts, bmrsa, "bo-", label="BMRSA")

    legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')

    plt.title("Decryption time vs Key Size in bits for batch size = " + str(bsize))
    plt.xlabel('Time in milliseconds')
    plt.ylabel('No of Bits in key')
    plt.show()
    bsize += 1
