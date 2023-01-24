# import sys

# n = int(input())

# l = [0] * 10000

# for i in range(n):
#     l[i] = int(sys.stdin.readline())

# l.sort()

# for i in l:
#     if i == 0: continue
#     sys.stdout.write(str(i) + '\n')

from random import random
import sys

n = 10000

l = [0] * 10000

for i in range(n):
    l[i] = int(random()*100)

l.sort()

for i in l:
    if i == 0: continue
    sys.stdout.write(str(i) + '\n')
