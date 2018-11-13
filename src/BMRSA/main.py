import mainBMRSA as Bmrsa
import mainMRSA as Mrsa
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
    pts = []

    # go till 18 bits
    # No of bits in key = 2 ** (n/b) * b
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

        # Get time for each MRSA
        for i in range(ll):
            timeMRSA += Mrsa.main(primes, es[i], m[i])

        # Time in milliseconds
        mrsa.append(timeMRSA*1000)

        # Get time for BMRSA
        timeBMRSA = Bmrsa.main(primes, es, m)

        # Time in milli seconds
        bmrsa.append(timeBMRSA*1000)

        itr += 2

    # Plotting graphs
    fig, ax = plt.subplots()

    # plot subplots
    ax.plot(pts, mrsa, "ro-", label="MRSA")
    ax.plot(pts, bmrsa, "bo-", label="BMRSA")

    # legends in graph
    legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')

    # title
    plt.title("Decryption time vs Key Size in bits for batch size = " + str(bsize))
    plt.xlabel('Time in milliseconds')
    plt.ylabel('No of Bits in key')

    # display graph
    plt.show()

    # increase byte size
    bsize += 1
