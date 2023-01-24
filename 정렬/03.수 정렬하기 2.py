import sys

arr_size = int(input())

result = []
for i in range(arr_size):
    result.append(int(sys.stdin.readline()))

result.sort()
for i in result:
    sys.stdout.write(str(i)+'\n')