n=int(input())
for _ in range(n):
    x=int(input())
    for i in range(1,x+1):
        for j in range(1,2*x+1):
            if(i<=x and j<=i) or (i<=x and j>(2*x-i)):
                print("*", end="")
            else:
                print("#", end="")
        print()

