import sys

# 문제를 입력
n = int(input())
l = list()
for i in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))


# 종료 시간을 기준으로 정렬
l.sort(key = lambda x: (x[1],x[0]))

# 중복된 강의를 제거
res = list()
for i in l:
    if len(res) <= 0 or res[-1][1] <= i[0]:
        res.append(i)  

print(len(res))