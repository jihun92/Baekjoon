arr_size = int(input())

result = []
for i in range(arr_size):
    result.append(int(input()))
for i in sorted(result):
    print(i)