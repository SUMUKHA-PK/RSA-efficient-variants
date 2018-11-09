import time
import sys
import os
from pathlib import Path
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), os.pardir))))
from EAMRSA import main as EAMRSA

plain_t = "the quick brown fox jumps over something"

t1s = time.time()
EAMRSA.run(12,128,3,6,plain_t)
t1e = time.time()

print("Time taken for 2304 bits: ",end="")
print(t1e-t1s)

t2s = time.time()
EAMRSA.run(16,128,4,4,plain_t)
t2e = time.time()

print("Time taken for 2048 bits: ",end="")
print(t2e-t2s)

t3s = time.time()
EAMRSA.run(16,256,4,5,plain_t)
t3e = time.time()

print("Time taken for 2560 bits: ",end="")
print(t3e-t3s)

t4s = time.time()
EAMRSA.run(12,128,3,8,plain_t)
t4e = time.time()

print("Time taken for 3072 bits: ",end="")
print(t4e-t4s)
