n_size = int(input())
n = set(map(int, input().split()))
m_size = int(input())
m = list(map(int, input().split()))

for i in m:
    if i in n:
        print(1)
    else:
        print(0)
