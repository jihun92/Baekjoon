t_size = int(input())

nums = list()
for i in range(t_size):
    
    n = int(input())
    
    if n != 0:
        nums.append(n)
    else :
        nums.pop()
    

print(sum(nums))