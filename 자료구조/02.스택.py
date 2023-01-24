n = int(input())

s = list()
cmd = list()
for i in range(n):
    cmd.append(input())

for i in cmd:
    if 'push' in i:
        num = int(i.split()[-1])
        s.append(num)
    elif i == 'pop':
        if s:
            print(s.pop())
        else:
            print(-1)
    elif i == 'size':
        print(len(s))
    elif i == 'empty':
        if len(s) == 0:
            print(1)
        else:
            print(0)
    elif i == 'top':
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])
