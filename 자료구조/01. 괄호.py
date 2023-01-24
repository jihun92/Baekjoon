n = int(input())

l = list()
for i in range(n):
    l.append(list(input()))


res = list()
for i in l:
    tmp = list()
    for j in i:
        if j == '(':
            tmp.append(j)
            continue
        else:
            if len(tmp) > 0:
                tmp.pop()
                continue
            else:
                tmp.append(j)
                break

    if len(tmp) == 0:
        res.append("YES")
    else:
        res.append("NO")

for i in res:
    print(i)