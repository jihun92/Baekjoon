n = input()
l = sorted(list(map(int, input().split())))

result = int()
for i in range(len(l)):
    result += sum(l[:i+1])

print(result)
