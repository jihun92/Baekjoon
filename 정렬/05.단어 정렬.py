n = int(input())
l = list()
for i in range(n):
    wrd = input()
    l.append( (len(wrd), wrd) )

l = sorted(set(l))
    
for i in l:
    print(i[1])