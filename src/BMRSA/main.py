import mainBMRSA as Bmrsa
import mainMRSA as Mrsa

from useful import funcs

n = 30
b = 2
ll = 2

primes = funcs.generate_primes(n, b)

n = 1

for p in primes:
    n *= p

m = funcs.generate_message(ll, n)

es = funcs.es(primes, ll)

timeMRSA = 0

for i in range(ll):
    timeMRSA += Mrsa.main(primes, es[i], m[i])

timeBMRSA = Bmrsa.main(primes, es, m)

print(timeMRSA, timeBMRSA)
