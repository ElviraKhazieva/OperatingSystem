#!/usr/bin/python3
import os
import sys
import random
import time

print(f"Child process started witn pid {os.getpid()} with argument {sys.argv[1]}")
time.sleep(int(sys.argv[1]))
print(f"Child process with pid {os.getpid()} finished")
exit(random.choice([0, 1]))

