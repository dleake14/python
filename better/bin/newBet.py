import time
import random
import sys

for x in range(5):
    if x >= 1: print("\n", end='')
    for x in range(25):
        this = random.randint(0,1)
        print(this, end='')
        sys.stdout.flush()
        time.sleep(.0005)
print("\n", end='')
