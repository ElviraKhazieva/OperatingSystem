#!/usr/bin/python3
import os
import sys
import random

print("Start")
child = 1
n = int(sys.argv[1])
print(f"Creating {n} processes")
for i in range(n):
	if child == 0:
		break
	child = os.fork()
if child > 0 :
	print('im waiting')
	ret = os.wait()
	print(f"Child process {ret[0]} finished with code {ret[1]}")
else:
	os.execl('child.py', "child.py", str(random.choice(range(5, 10))))



