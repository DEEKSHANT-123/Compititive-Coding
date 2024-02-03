n = int(input())
a = list(map(int, input().split()))
c=0
d=0
e=0
for i in a:
    if i>0:
        c=c+1
    elif i<0:
        d=d+1
    else:
        e=e+1
print(c/n)
print(d/n)
print(e/n)
    
