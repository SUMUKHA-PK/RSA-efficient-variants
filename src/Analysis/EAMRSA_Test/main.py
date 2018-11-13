import time
import sys
import os
from pathlib import Path
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), os.pardir))))
from EAMRSA import main as EAMRSA
from Simple_RSA import main as SRSA
from matplotlib import pyplot as plt

Times = []
plain_t = "number theory mini project"


Time1 = []
Time2 = []
Time13 = []
Time23 = []
Time14 = []
Time24 = []

t2s = time.time()
EAMRSA.run(18,3,3,256,plain_t)
t2e = time.time()

print("Time taken for 2048 bits EA1RSA(b=3): ",end="")
Time1.append(t2e-t2s)
print(t2e-t2s)

t5s = time.time()
EAMRSA.run(18,2,4,256,plain_t)
t5e = time.time()

print("Time taken for 2048 bits EA2RSA(b=4): ",end="")
Time2.append(t5e-t5s)
print(t5e-t5s)

t6s = time.time()
EAMRSA.run(18,6,3,128,plain_t)
t6e = time.time()

print("Time taken for 2048 bits EA1M3RSA (b=3,c=128): ",end="")
Time13.append(t6e-t6s)
print(t6e-t6s)

t7s = time.time()
EAMRSA.run(18,4,4,128,plain_t)
t7e = time.time()

print("Time taken for 2048 bits EA1M4RSA (b=4,c=128): ",end="")
Time14.append(t7e-t7s)
print(t7e-t7s)

t3s = time.time()
EAMRSA.run(18,3,3,256,plain_t)
t3e = time.time()

print("Time taken for 2048 bits EA2M3RSA(b=3,c=256): ",end="")
Time23.append(t3e-t3s)
print(t3e-t3s)

t4s = time.time()
EAMRSA.run(18,2,4,256,plain_t)
t4e = time.time()

print("Time taken for 2048 bits EA2M4RSA(b=4,c=256): ",end="")
Time24.append(t4e-t4s)
print(t4e-t4s)

#------------------------------------------------------------------2048 bits done------------------------------------------------------

t2s = time.time()
EAMRSA.run(18,3,3,256,plain_t)
t2e = time.time()

print("Time taken for 2304 bits EA1RSA(b=3): ",end="")
Time1.append(t2e-t2s)
print(t2e-t2s)

t5s = time.time()
EAMRSA.run(18,8,4,96,plain_t)
t5e = time.time()

print("Time taken for 2304 bits EA2RSA(b=4): ",end="")
Time2.append(t5e-t5s)
print(t5e-t5s)

t6s = time.time()
EAMRSA.run(18,6,3,128,plain_t)
t6e = time.time()

print("Time taken for 2304 bits EA1M3RSA (b=3,c=128): ",end="")
Time13.append(t6e-t6s)
print(t6e-t6s)

t7s = time.time()
EAMRSA.run(18,5,4,128,plain_t)
t7e = time.time()

print("Time taken for 2304 bits EA1M4RSA (b=4,c=128): ",end="")
Time14.append(t7e-t7s)
print(t7e-t7s)

t3s = time.time()
EAMRSA.run(18,3,3,256,plain_t)
t3e = time.time()

print("Time taken for 2304 bits EA2M3RSA(b=3,c=256): ",end="")
Time23.append(t3e-t3s)
print(t3e-t3s)

t4s = time.time()
EAMRSA.run(18,3,4,256,plain_t)
t4e = time.time()

print("Time taken for 2304 bits EA2M4RSA(b=4,c=256): ",end="")
Time24.append(t4e-t4s)
print(t4e-t4s)


#--------------------------------------------------------------------2304 bits done-------------------------------------------------------

t2s = time.time()
EAMRSA.run(18,5,2,256,plain_t)
t2e = time.time()

print("Time taken for 2560 bits EA1RSA(b=3): ",end="")
Time1.append(t2e-t2s)
print(t2e-t2s)

t5s = time.time()
EAMRSA.run(18,5,4,128,plain_t)
t5e = time.time()

print("Time taken for 2560 bits EA2RSA(b=4): ",end="")
Time2.append(t5e-t5s)
print(t5e-t5s)

t6s = time.time()
EAMRSA.run(18,7,3,128,plain_t)
t6e = time.time()

print("Time taken for 2560 bits EA1M3RSA (b=3,c=128): ",end="")
Time13.append(t6e-t6s)
print(t6e-t6s)

t7s = time.time()
EAMRSA.run(18,5,4,128,plain_t)
t7e = time.time()

print("Time taken for 2560 bits EA1M4RSA (b=4,c=128): ",end="")
Time14.append(t7e-t7s)
print(t7e-t7s)

t3s = time.time()
EAMRSA.run(18,4,3,256,plain_t)
t3e = time.time()

print("Time taken for 2560 bits EA2M3RSA(b=3,c=256): ",end="")
Time23.append(t3e-t3s)
print(t3e-t3s)

t4s = time.time()
EAMRSA.run(18,3,4,256,plain_t)
t4e = time.time()

print("Time taken for 2560 bits EA2M4RSA(b=4,c=256): ",end="")
Time24.append(t4e-t4s)
print(t4e-t4s)

#--------------------------------------------------------------2560 bits done-----------------------------------------

t2s = time.time()
EAMRSA.run(18,4,3,256,plain_t)
t2e = time.time()

print("Time taken for 2860 bits EA1RSA(b=3): ",end="")
Time1.append(t2e-t2s)
print(t2e-t2s)

t5s = time.time()
EAMRSA.run(18,5,4,128,plain_t)
t5e = time.time()

print("Time taken for 2860 bits EA2RSA(b=4): ",end="")
Time2.append(t5e-t5s)
print(t5e-t5s)

t6s = time.time()
EAMRSA.run(18,7,3,128,plain_t)
t6e = time.time()

print("Time taken for 2860 bits EA1M3RSA (b=3,c=128): ",end="")
Time13.append(t6e-t6s)
print(t6e-t6s)

t7s = time.time()
EAMRSA.run(18,5,4,128,plain_t)
t7e = time.time()

print("Time taken for 2860 bits EA1M4RSA (b=4,c=128): ",end="")
Time14.append(t7e-t7s)
print(t7e-t7s)

t3s = time.time()
EAMRSA.run(18,4,3,256,plain_t)
t3e = time.time()

print("Time taken for 2860 bits EA2M3RSA(b=3,c=256): ",end="")
Time23.append(t3e-t3s)
print(t3e-t3s)

t4s = time.time()
EAMRSA.run(18,3,4,256,plain_t)
t4e = time.time()

print("Time taken for 2860 bits EA2M4RSA(b=4,c=256): ",end="")
Time24.append(t4e-t4s)
print(t4e-t4s)

#-------------------------------------------------------2860 bits done---------------------------------------------3072
t2s = time.time()
EAMRSA.run(18,7,3,128,plain_t)
t2e = time.time()

print("Time taken for 3072 bits EA1RSA(b=3): ",end="")
Time1.append(t2e-t2s)
print(t2e-t2s)

t5s = time.time()
EAMRSA.run(18,6,4,128,plain_t)
t5e = time.time()

print("Time taken for 3072 bits EA2RSA(b=4): ",end="")
Time2.append(t5e-t5s)
print(t5e-t5s)

t6s = time.time()
EAMRSA.run(18,7,3,128,plain_t)
t6e = time.time()

print("Time taken for 3072 bits EA1M3RSA (b=3,c=128): ",end="")
Time13.append(t6e-t6s)
print(t6e-t6s)

t7s = time.time()
EAMRSA.run(18,6,4,128,plain_t)
t7e = time.time()

print("Time taken for 3072 bits EA1M4RSA (b=4,c=128): ",end="")
Time14.append(t7e-t7s)
print(t7e-t7s)

t3s = time.time()
EAMRSA.run(18,4,3,256,plain_t)
t3e = time.time()

print("Time taken for 3072 bits EA2M3RSA(b=3,c=256): ",end="")
Time23.append(t3e-t3s)
print(t3e-t3s)

t4s = time.time()
EAMRSA.run(18,3,4,256,plain_t)
t4e = time.time()

print("Time taken for 3072 bits EA2M4RSA(b=4,c=256): ",end="")
Time24.append(t4e-t4s)
print(t4e-t4s)

#--------------------------------------------------------------------3072 bits done------------------------------------------------------------

bits = [2048,2304,2560,2816,3072]


plt.plot(bits,Time1, label='EA1RSA')
plt.plot(bits,Time2, label='EA2RSA')
plt.plot(bits,Time13, label='EA1M3RSA')
plt.plot(bits,Time14, label='EA1M4RSA')
plt.plot(bits,Time23, label='EA2M3RSA')
plt.plot(bits,Time24, label='EA2M4RSA')

plt.xlabel('Number of bits')
plt.ylabel('Time taken')

plt.legend()

plt.show()