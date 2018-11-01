import time
import sys
import os
from pathlib import Path
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), os.pardir))))
from EAMRSA import main as EAMRSA

EAMRSA.run(30,5,2,3)