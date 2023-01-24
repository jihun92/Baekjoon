n = int(input())

l = list()
for i in range(n):
    age, name = input().split()
    l.append([i,int(age),name])

l.sort(key=lambda x : (x[1], x[0]))

for i in l:
    print(i[1],i[2])