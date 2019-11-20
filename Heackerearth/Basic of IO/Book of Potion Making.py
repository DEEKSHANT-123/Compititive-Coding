n=input()
c=1
s=0
if len(n)==10:
    for i in range(len(n)):
        x=int(n[i])*c
        c=c+1
        s=s+x
    if s%11==0:
        print("Legal ISBN")

else:
    print("Illegal ISBN")
