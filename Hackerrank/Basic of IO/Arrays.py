n=int(input())
c=0
a=list(map(int, input().split()))
for i in range(n):
    j=n-i-1
    print(a[j], end=" ")
