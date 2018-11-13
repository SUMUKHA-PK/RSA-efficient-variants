import time
import sys
import os
from pathlib import Path
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))))

from Simple_RSA import main as Simple_RSA

SRSA_start = time.time()
Simple_RSA.run(2467,2473,"the quick brown fox jumped over the lazy dog")
SRSA_end = time.time()

print("Simple RSA took: ",end="")
print(SRSA_end-SRSA_start)

# There will be a same input comparison between all RSAs and also a comparison between different variants in the RSA