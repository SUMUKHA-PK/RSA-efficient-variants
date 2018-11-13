import mainBMRSA as Bmrsa
import mainBRSA as Brsa
import matplotlib.pyplot as plt

from useful import funcs


# number of bs
bsize = 1


while bsize < 4:

    # Start from prime size = 10 bits
    # mrsa and bmrsa time
    itr = 10
    mrsa = []
    bmrsa = []

    # points needed to be marked on graph
    pts = [1024]

    # go till 18 bits
    # No of bits in key = 2 ** (n/b) * b
    while itr <= 18:

        n = itr
        b = 2
        ll = bsize

        primes = funcs.generate_primes(n, b)

        n = 1

        for p in primes:
            n *= p

        m = funcs.generate_message(ll, n)

        es = funcs.es(primes, ll)

        timeBRSA = 0

        # Get time for each BRSA
        for i in range(ll):
            timeBRSA += Brsa.main(primes, es[i], m[i])

        # Time in milliseconds
        mrsa.append(timeBRSA * 1000)

        # Get time for BMRSA
        timeBMRSA = Bmrsa.main(primes, es, m)

        # Time in milli seconds
        bmrsa.append(timeBMRSA*1000)

        pts = [1024, 1536, 2048, 2560, 3072]

        itr += 2

    # Plotting graphs
    fig, ax = plt.subplots()

    # plot subplots
    ax.plot(pts, mrsa, "ro-", label="BatchRSA")
    ax.plot(pts, bmrsa, "bo-", label="BMRSA")

    # legends in graph
    legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')

    # title
    plt.title("Decryption time vs Key Size in bits for batch size = " + str(bsize))
    plt.ylabel('Time in milliseconds')
    plt.xlabel('No of Bits in key')

    # display graph
    plt.show()

    # increase byte size
    bsize += 1
