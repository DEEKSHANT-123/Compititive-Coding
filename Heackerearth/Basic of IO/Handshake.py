T=int(input())
for _ in range(T):
    n=int(input())
    c=1    
    d=1    # c and d both are veriables used for calculation.
    for i in range(2,n-1):
        c=c*i
    for j in range(2,n+1):
        d=d*j
    print(int(d/(c*2)))


