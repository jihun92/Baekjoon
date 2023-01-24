n = int(input())

l = list()
for i in range(n):
    xy = list(map(int, input().split()))
    l.append(xy)

l.sort()
for i in l:
    print(i[0],i[1])