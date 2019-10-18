n=list(map(int, input().split()))
m=list(map(int, input().split()))
x=0
y=0
c=0
d=0
for i in n:
    x=x+1
for j in m:
    y=y+1
for g in range(3):
    if n[g]>m[g]:
        c=c+1
    elif n[g]<m[g]:
        d=d+1
    else:
        d=d
print(c,d)
